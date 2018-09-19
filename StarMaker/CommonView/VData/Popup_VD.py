# coding=utf-8
from Utils import Tools
package = Tools.Tools().package()
FindSource = Tools.Tools().FindSource
# ----------
# 弹窗汇总
# ----------

# 通用——关闭弹窗
Source_Popup_ImgClose_ID = "img_close"
Popup_ImgClose_ID = package + FindSource(Source_Popup_ImgClose_ID)

# ----------
# 1>首页弹窗
# ----------

# ①登陆后首页 New Feature 引导（New Feature[0]/Share your pictures and view what's shared by others.[1]/OK按钮[2]）
Popup_NewFeature_Class = "android.widget.TextView"

# ②③登陆后首页 Ranking/Parties 引导 文案（text="Ranking and Hashtag are moved here"/Parties are moved here）
Source_Popup_GuideText_ID = "content_tv"
Popup_Guide_Text_ID = package + FindSource(Source_Popup_GuideText_ID)

# ②③登陆后首页 Ranking/Parties 引导 NEXT按钮/DONE按钮
Source_Popup_Guide_Next_ID = "next_tv"
Popup_Guide_Next_ID = package + FindSource(Source_Popup_Guide_Next_ID)

# 签到按钮，如果存在，需点击通用close按钮
Source_Popup_CheckIn_ID = "btn_check_in"
Popup_CheckIn_ID = package + FindSource(Source_Popup_CheckIn_ID)

# ----------
# 2>Profile页弹窗
# ----------

# 验证邮箱弹窗，如果存在，需点击通用close按钮
Source_Popup_VerifyEmail_Verify_ID = "tv_email_verify"
Popup_VerifyEmail_Verify_ID = package + FindSource(Source_Popup_VerifyEmail_Verify_ID)

# ----------
# 3>点唱页页弹窗
# ----------

# 发布图片引导(text=Click to post a photo)/发布图片+文字引导(text=Post texts with background photo.)
Source_Popup_PostGuide_ID = "text"
Popup_PostGuide_ID = package + FindSource(Source_Popup_PostGuide_ID)