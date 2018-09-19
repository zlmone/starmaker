# coding=utf-8
import time
import unittest
from CommonView.StartUp import StartUp
from CommonView.LogIn import LogIn
from CommonView.Home import Home
from CommonView.SignUp import SignUp
from Utils.Tools import Tools
from Utils.GetAppiumDeriver import GetAppiumDeriver
from Utils.ReadXMLData import ReadXMLData


# 邮箱登录
class EmailLogInCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetAppiumDeriver().driver
        time.sleep(5)

    def setUp(self):
        time.sleep(1)

    def tearDown(self):
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        pass

    # Email登录输入框功能验证——清空Email
    def test_Case001_InputFunction_ClearingEmailCase(self):
        # 点击邮箱登录按钮
        StartUp().Email_LogIn_Btn_R()
        # 点击登录弹窗中LogIn按钮
        LogIn().EmailWindow_LogIn_Btn().click()
        time.sleep(1)
        # 输入邮箱
        LogIn().Email_Username_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Email"))
        time.sleep(1)
        # 点击清空Email
        LogIn().Email_Clear_EmailBox_Btn().click()
        time.sleep(1)
        expValue = ""
        # 获取账号输入框内容
        actValue = LogIn().Email_Username_Box().text
        # 判断账号输入框为空
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # Email登录输入框功能验证——清空Pwd
    def test_Case002_InputFunction_ClearingPasswordCase(self):
        # 输入密码
        LogIn().Email_Password_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password"))
        time.sleep(1)
        # 点击清空Pwd
        LogIn().Email_Clear_PWDBox_Btn().click()
        time.sleep(1)
        expValue = ""
        # 获取密码输入框内容
        actValue = LogIn().Email_Password_Box().text
        # 判断密码输入框为空
        time.sleep(1)
        self.assertEqual(expValue, actValue)
        LogIn().Email_Password_Box().clear()

    # Email登录输入框功能验证——展示明文密码
    def test_Case003_InputFunction_ShowPasswordCase(self):
        # 输入密码
        LogIn().Email_Password_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password"))
        time.sleep(1)
        # 点击展示明文密码
        LogIn().Email_ShowPassword_Btn().click()
        time.sleep(1)
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password")
        # 获取密码输入框内容（非明文text：••••••/明文text：000000）
        actValue = LogIn().Email_Password_Box().text
        # 判断是否成功展示明文密码
        time.sleep(1)
        self.assertEqual(expValue, actValue)
        LogIn().Email_Password_Box().clear()

    # Email登录——未输入账号时忘记密码光标焦到账户输入框
    def test_Case004_ForgotPassword_FocusedCase(self):
        # 点击忘记密码
        LogIn().Email_ForgotPassword_Link().click()
        time.sleep(1)
        expValue = "true"
        # 因未输入密码，光标聚焦到账号输入框
        actValue = LogIn().Email_Username_Box().get_attribute("focused")
        # 判断光标是否成功聚焦
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # Email登录——未输入账号时忘记密码输入框下方提示不能为空：Your email cannot be empty.
    def test_Case005_ForgotPassword_EmailError_EmptyCase(self):
        expValue = "Your email cannot be empty."
        # 获取账号输入框下方Error提示
        actValue = LogIn().Email_Username_Error().text
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # Email登录——账号错误提示：未注册
    def test_Case006_EmailError_NotRegisteredCase(self):
        # 输入未注册账号/密码
        LogIn().Email_Username_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "NotRegisteredEmail"))
        LogIn().Email_Password_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password"))
        time.sleep(1)
        # 点击登录按钮
        LogIn().LogIn_Confirm_Btn().click()
        time.sleep(1)
        expValue = "This Email is not registered yet, please Sign Up now."
        # 获取账号输入框下方Error提示
        actValue = LogIn().Email_Username_Error().text
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # Email登录——Sign Up跳转注册页
    def test_Case007_EmailError_SignUp_linkCase(self):
        # 输入未注册账号/密码
        LogIn().Email_Username_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "NotRegisteredEmail"))
        LogIn().Email_Password_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password"))
        time.sleep(1)
        # 点击登录按钮
        LogIn().LogIn_Confirm_Btn().click()
        time.sleep(5)
        # 点击SignUp
        LogIn().Email_Username_SignUpNow_ACP()
        # self.driver.tap([(1030, 650)], 500)
        time.sleep(1)
        expValue = "输入邮箱"
        # 获取注册页Tips值
        actValue = SignUp().SignUp_Tips().text
        # 验证是否跳转成功
        time.sleep(1)
        self.assertEqual(expValue, actValue)
        # 为Email登录Case 执行tearDown:
        # 1.返回
        self.driver.back()
        time.sleep(10)
        # 2.点击邮箱登录按钮
        StartUp().Email_LogIn_Btn_R()
        time.sleep(1)
        # 3.点击登录弹窗中LogIn按钮
        LogIn().EmailWindow_LogIn_Btn().click()
        time.sleep(1)

    # Email登录——密码错误提示
    def test_Case008_EmailError_PwdIncorrect(self):
        # 输入邮箱
        LogIn().Email_Username_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Email"))
        # 输入错误密码
        LogIn().Email_Password_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "IncorrectPassword"))
        # 点击LogIn
        LogIn().LogIn_Confirm_Btn().click()
        time.sleep(5)
        expValue = "Username or password is incorrect"
        # 获取密码输入框下方Error提示
        actValue = LogIn().Email_Password_Error().text
        # 判断是否提示密码输入错误
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # Email登录——新装包首次登录成功
    def test_Case008_EmailLogIn(self):
        # 输入邮箱
        LogIn().Email_Username_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Email"))
        # 输入密码
        LogIn().Email_Password_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password"))
        # 点击LogIn
        LogIn().LogIn_Confirm_Btn().click()
        time.sleep(5)
        expValue = "Share your pictures and view what's shared by others."
        # 记录首页New Feature引导文案
        actValue = Home().HomePage_NewFeature_Tips().text
        # 判断是否新装包首次登录成功——展示New Feature引导
        time.sleep(1)
        self.assertEqual(expValue, actValue)


# if __name__ == "__main__":
#     pass