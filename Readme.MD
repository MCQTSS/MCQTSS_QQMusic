# QQ音乐解析

### CodeBy MCQTSS

# 包含文件&使用的第三方库&Python版本

| 文件名       | 作用  |
|:----------|:----|
| Readme.MD | 说明  |
| Main.py   | 主程序 |
| demo.py   | 演示  |

| 名称       | 版本     |
|:---------|:-------|
| Python   | 2.9    |
| requests | 2.27.1 |

# 函数&类作用

| 类名       | 作用     |
|:---------|:-------|
| QQ_Music | 存放主要函数 |

| 文件名            | 作用                               | 需要提交参数                                                                            |
|:---------------|:---------------------------------|-----------------------------------------------------------------------------------|
| set_cookie     | 设置Cookie(吧Cookie转换为Python字典格式)   | Cookie:获取方式请参考[如何获取Cookie](#如何获取Cookie)                                           |
| get_music_url  | 通过音乐MID解析音乐播放URL                 | music_mid:音乐的MID,https://y.qq.com/n/ryqq/songDetail/xxx (xxx就是这首歌的MID)或搜索返回结果时会返回 |
| get_song_info  | 通过搜索返回的音乐ID来获取当前音乐信息(MID,曲名,专辑名) | music_id:音乐ID,搜索返回的结果有                                                            |
| get_album_info | 通过专辑MID获取专辑信息,MID在搜索,获取音乐信息时返回   | album_mid:专辑MID                                                                   |
| search_music   | 搜索音乐                             | name:要搜索的音乐名 limit:返回的音乐数量                                                        |

# 如何获取Cookie

#### 1.打开 [QQ音乐官网](https://y.qq.com/) 后登录QQ音乐

#### 2.按下F12或右键检测打开开发者工具并选择网络选项(部分浏览器叫Network)

#### 3.按Ctrl+R刷新网页后在Fetch/XHR中随便找一个让后打开他的标头(Headers)

#### 4.在请求标头(RequestHeaders)中找到Cookie并右键复制即可

#### Tips:Cookie有过期时间,只有绿钻的Cookie才能解析绿钻歌曲

<img alt="截图" heig ht="296" src="MD/截图.png" width="512"/></br>

# 赞助

### [爱发电](https://afdian.net/@mcqtss)

### 支付宝

<img src="docs/zfb.jpg" width="111px" height="165px" alt="支付宝">

### 微信

<img src="docs/wx.jpg" width="111px" height="157px" alt="微信">
