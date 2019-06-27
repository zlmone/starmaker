# encoding=utf-8
"""
用于生成内存使用报告

开始前内存占用
结束后内存占用
| 平均内存占用 | 最大内存占用 |
"""
import datetime
import json
import os
import sys
import time

root_dir = os.path.realpath(os.path.realpath(__file__) + "/../.." + "/report")
os.chdir(root_dir)


# 重定向日志，将print日志输出到控制台和日志文件里面
# TODO：重新封装日志写入；
class logger:
    def __init__(self, data_type='events'):
        self.__console__ = sys.stdout

        log_dir = os.path.join(root_dir, '.logs')
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        self.file_logger = open(
            os.path.join(log_dir, "./%s-logs-%s.log" % (data_type, datetime.datetime.now().strftime('%Y%m%d')))
            , 'a+', encoding='utf-8')
        self.detail_file_logger = open(
            os.path.join(log_dir, "./%s-logs-details-%s.log" % (data_type, datetime.datetime.now().strftime('%Y%m%d')))
            , 'a+', encoding='utf-8')

        sys.stdout = self

    def write(self, output_stream):
        # self.__console__.write(output_stream)
        self.file_logger.write(output_stream)
        self.file_logger.flush()

    def detail(self, output_stream):
        self.detail_file_logger.write(output_stream)
        self.detail_file_logger.flush()

    def reset(self):
        sys.stdout = self.__console__

    def flush(self):
        pass


r_logger = logger


class AndroidMemoryReport:
    def __init__(self, appPackage, driver):
        self.memInfos = []
        self.data_type = ""
        self.appPackage = appPackage
        self.driver = driver

    # 记录当前内存占用情况
    def profile(self):
        self.data_type = "memoryinfo"
        try:
            memInfo = self.driver.get_performance_data(self.appPackage, self.data_type, 5)
            self.memInfos.append(memInfo)
            self.saveRawToFile(memInfo)
        except Exception as e:
            print("get_memoryinfo_error:", e)

    def clear(self):
        self.memInfos = []

    # 保存原始数据到文件
    def saveRawToFile(self, Info):
        r_logger(self.data_type).detail(json.dumps(Info, indent=2))

    # 保存测试数据到文件
    def saveTestData(self, Info):
        r_logger(self.data_type).write(json.dumps(Info, indent=2))

    # 生成内存报告
    def toReport_memInfos(self, module_name):
        m = self.memInfos[0]
        totalPssIndex = m[0].index('totalPss')

        startMemory = self.memInfos[0][1][totalPssIndex]
        endMemory = self.memInfos[-1][1][totalPssIndex]

        totalMemory = 0
        maxMemory = 0
        for m in self.memInfos[1:-2]:
            c = int(m[1][totalPssIndex])
            totalMemory += c
            if c > maxMemory:
                maxMemory = c

        averageMemory = int(float(totalMemory/(len(self.memInfos) - 2)))
        module = module_name + " memInfos_Report"
        print(module)
        print("\n""------------------------------")
        print('%20s: %s' % ('startMemory', startMemory.__str__()))
        print('%20s: %s' % ('endMemory', endMemory.__str__()))
        print('%20s: %s' % ('averageMemory', averageMemory.__str__()))
        print('%20s: %s' % ('maxMemory', maxMemory.__str__()))
        print("------------------------------""\n")
        time.sleep(2)

        self.clear()
