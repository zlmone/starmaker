# coding=utf-8
#from Utils.GetDevicesInfo import GetPackages
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
# ----------
# 启动模块
# ----------

# 语言选择页-校验启动成功-顶部Tips文案([0]text=Choose Language)
ChooseLanguagePage_CheckStartSuccess_Tips_ClaS = "android.widget.TextView"

# 语言选择页-选择语言-[通用]([1]text=हिन्दी/[2]text=বাংলা/[3]text=ಕನ್ನಡ/[4]text=தமிழ்/[5]text=ગુજરાતી/[6]text=ଓଡ଼ିଆ/[7]text=മലയാളം
# /[8]text=मराठी/[9]text=తెలుగు/[10]text=ਪੰਜਾਬੀ/[11]text=অসমীয়া/[12]text=हरियाणवी/[13]text=राजस्थानी/[14]text=भोजपूरी/[15]text=English)
ChooseLanguagePage_SelectLanguage_Common_ClaS = "android.widget.TextView"
