# coding=utf-8
"""
调整测试数据
依次运行对应测试脚本
"""
import argparse
import time

from automation_3.report.test_data_extraction import get_data


class testSuite:
    # 测试数据调整
    def __init__(self):
        try:
            parser = argparse.ArgumentParser()
            # 版本信息
            parser.add_argument("version")
            # 待测包名
            parser.add_argument("package")
            # 设备信息
            parser.add_argument("platformVersion")
            parser.add_argument("device")
            parser.add_argument("deviceName")

            args = parser.parse_args()

            param = vars(args)

            v = {}

            for key, value in param.items():
                v[key] = value

            # 测试版本
            self.ver = v["version"]
            # 包信息
            self.package = v["package"]
            # 设备信息
            self.platformVersion = v["platformVersion"]
            self.device = v["device"]
            self.deviceName = v["deviceName"]
        except:
            # 测试版本
            self.ver = "9.9.9"
            # 包信息
            self.package = "Sargam"
            # 设备信息
            self.platformVersion = "8.1.0"
            self.device = "vivo_1716"
            self.deviceName = "1716"

        # 取数据次数（最低5，因为结算时会减去最高和最低）
        self.num = 10
        # 单次数据运行时间
        self.run_time = 10
        # 录制歌曲数量
        self.song_num = 2

    # 测试数据处理
    def log_result(self, modular):
        result = get_data(self.ver, modular)
        if result:
            print("%s模块数据已记录成功" % modular)
        time.sleep(10)

    def liveSuite(self):
        from automation_3.live.performance_broadcaster import PerformanceBroadcaster
        modular = "live"
        num = 0
        while num < self.num:
            num += 1
            print("\n\n当前运行 %s模块 第%s次" % (modular, num))
            try:
                PerformanceBroadcaster().suiteRunner(PerformanceBroadcaster)
            except ValueError:
                num -= 1
                continue
        self.log_result(modular)

    def momentSuite(self):
        from automation_3.moment.performance_popular import PerformanceMoment
        modular = "popular"
        num = 0
        while num < self.num:
            num += 1
            print("\n\n当前运行 %s模块 第%s次" % (modular, num))
            try:
                PerformanceMoment().suiteRunner(PerformanceMoment)
            except ValueError:
                num -= 1
                continue
        self.log_result(modular)

    def recordingSuite(self):
        from automation_3.recording.performance_recording import PerformanceRecording
        modular = "recording"
        num = 0
        while num < self.num:
            num += 1
            print("\n\n当前运行 %s模块 第%s次" % (modular, num))
            try:
                PerformanceRecording().suiteRunner(PerformanceRecording)
            except ValueError:
                num -= 1
                continue
        self.log_result(modular)


if __name__ == '__main__':
    testSuite().liveSuite()
    testSuite().momentSuite()
    testSuite().recordingSuite()