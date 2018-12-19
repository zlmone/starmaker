# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FindSource = Tools.Tools().FindSource
FS = package + FindSource
# ----------
# Library页
# ----------

# Library页搜索框
Library_SearchBox_ID = "com.starmakerinteractive.starmaker:id/tv_search_fragment_sing_new"

# 歌曲信息(4个元素一组,组成一首歌曲信息)
# 1.第一组0-3为Tab；
# 2.第二组开始：[4]歌曲名/[5]上传用户/[6]歌手/[7]SING
LibraryPage_SongInfo_ClaS = "android.widget.TextView"

# 第二首歌曲——Sing按钮
LibraryPage_SecondSong_SingBtn_AUS = "new UiSelector().text(\"SING\")"

# Library页录制模式
LibraryPage_SongMode_ClaS = "android.widget.TextView"

# ----------
# 搜索页
# ----------

# 搜索页输入框
SearchPage_InputBox_ID = "com.starmakerinteractive.starmaker:id/searchView"

# ----------
# 歌曲详情页
# ----------

# 歌曲信息([0]歌曲名/[1]歌手/[2]上传用户/[3]SING)
SongInfoPage_SongInfo_ClaS = "android.widget.TextView"

# 选择录制类型([1]Solo/[2]Start Collab)
SongInfoPage_Type_ClaS = "android.widget.LinearLayout"
