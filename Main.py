import time
import base64
import requests
import json
import random
import re


class QQ_Music:
    def __init__(self):
        self._headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Referer': 'https://y.qq.com/',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 ('
                          'KHTML, like Gecko) Mobile/17D50 UCBrowser/12.8.2.1268 Mobile AliApp(TUnionSDK/0.1.20.3) '
        }
        self._cookies = {}

    def set_cookie(self, cookie):  # 网页Cookie转换到Python字典格式
        list_ret = {}
        cookie_list = cookie.split('; ')  # 分隔符
        for i in range(len(cookie_list)):
            list_1 = cookie_list[i].split('=')  # 分割等于后面的值
            list_ret[list_1[0]] = list_1[1]  # 加入字典
        return list_ret

    def get_music_url(self, music_mid):  # 通过Mid获取音乐播放URL
        uin = ''.join(random.sample('1234567890', 10))  # UIN基本不校验,长度10就行,如果请求正常这是你的QQ号
        data = {
            "req": {
                "module": "CDN.SrfCdnDispatchServer",
                "method": "GetCdnDispatch",
                "param": {
                    "guid": "1535153710",
                    "calltype": 0,
                    "userip": ""
                }
            },
            "req_0": {
                "module": "vkey.GetVkeyServer",
                "method": "CgiGetVkey",
                "param": {
                    "guid": "1535153710",
                    "songmid": [music_mid],
                    "songtype": [0],
                    "uin": uin,
                    "loginflag": 1,
                    "platform": "20",
                }
            },
            "comm": {
                "uin": uin,
                "format": "json",
                "ct": 24,
                "cv": 0
            }
        }  # 提交到QQ服务器的内容,还有种sign=xxx的写法没搞明白,搞明白了会加个_2方法
        ret = json.loads(requests.get('https://u.y.qq.com/cgi-bin/musicu.fcg?data={}'.format(json.dumps(data)),
                                      headers=self._headers, cookies=self._cookies).text)
        if ret['code'] == 500001:  # 如果返回500001表示提交的数据有问题或Cookie过期之类的(解析绿钻歌曲你不是绿钻也有可能给你这个)
            return 'Error'
        return 'https://dl.stream.qqmusic.qq.com/{}'.format(ret['req_0']['data']['midurlinfo'][0]['purl'])

    def get_music_info(self, music_id):  # 通过音乐的ID获取歌曲信息
        uin = ''.join(random.sample('1234567890', 10))
        data = {"comm": {"cv": 4747474, "ct": 24, "format": "json", "inCharset": "utf-8", "outCharset": "utf-8",
                         "notice": 0, "platform": "yqq.json", "needNewCode": 1, "uin": uin,
                         "g_tk_new_20200303": 708550273, "g_tk": 708550273},
                "req_1": {"module": "music.trackInfo.UniformRuleCtrl", "method": "CgiGetTrackInfo",
                          "param": {"ids": [music_id], "types": [0]}}}
        ret = json.loads(requests.get(url='https://u.y.qq.com/cgi-bin/musicu.fcg?data={}'.format(json.dumps(data)),
                                      headers=self._headers, cookies=self._cookies).text)
        if ret['code'] == 500001:  # 如果返回500001代表提交的数据有问题
            return 'Error'
        return ret['req_1']['data']['tracks']  # 直接返回QQ音乐服务器返回的结果,和搜索返回的感觉差不多,直接返回tracks数组\

    def get_album_info(self, album_mid):  # 获取专辑信息
        uin = ''.join(random.sample('1234567890', 10))  # 和音乐的那个一样,uin随机10个数字就行
        data = {"comm": {"cv": 4747474, "ct": 24, "format": "json", "inCharset": "utf-8", "outCharset": "utf-8",
                         "notice": 0, "platform": "yqq.json", "needNewCode": 1, "uin": uin,
                         "g_tk_new_20200303": 708550273, "g_tk": 708550273},
                "req_1": {"module": "music.musichallAlbum.AlbumInfoServer", "method": "GetAlbumDetail",
                          "param": {"albumMid": album_mid}}}
        resp = json.loads(requests.get(url='https://u.y.qq.com/cgi-bin/musicu.fcg?data={}'.format(json.dumps(data)),
                                       headers=self._headers, cookies=self._cookies).text)
        if resp['code'] == 500001:  # 如果返回500001代表提交的数据有问题
            return 'Error'
        return resp

    def search_music(self, name, limit=20):  # 搜索歌曲,name歌曲名,limit返回数量
        return requests.get(url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp', params={
            'w': name,
            't': 0,
            'n': limit,
            'page': 1,
            'cr': 1,
            'new_json': 1,
            'format': 'json',
            'platform': 'yqq.json'
        }, timeout=1, headers=self._headers).json()['data']['song']['list']

    def get_playlist_info(self, playlist_id):  # 通过歌单ID获取歌单信息,songList返回的内容和搜索返回的差不多
        return json.loads(str(re.findall('window.__INITIAL_DATA__ =(.*?)</script>',
                                         requests.get(url='https://y.qq.com/n/ryqq/playlist/{}'.format(playlist_id),
                                                      headers=self._headers,
                                                      cookies=self._cookies).text)[0]).replace('undefined',
                                                                                               '"undefined"'))

    def get_playlist_info_num(self, playlist_id, song_num):  # 逐个获取歌单ID内容
        data = {
            "req_0": {
                "module": "srf_diss_info.DissInfoServer",
                "method": "CgiGetDiss",
                "param": {
                    "disstid": playlist_id,
                    "onlysonglist": 1,
                    "song_begin": song_num,
                    "song_num": 15
                }
            },
            "comm": {
                "g_tk": 865217452,
                "uin": ''.join(random.sample('1234567890', 10)),
                "format": "json",
                "platform": "h5"
            }
        }
        resp = json.loads(requests.get(url='https://u.y.qq.com/cgi-bin/musicu.fcg?data={}'.format(json.dumps(data)),
                                       headers=self._headers, cookies=self._cookies).text)
        if resp['code'] == 500001:  # 如果返回500001代表提交的数据有问题
            return 'Error'
        return resp

    def get_recommended_playlist(self):  # 获取QQ音乐推荐歌单,获取内容应该和Cookie有关
        return json.loads(str(re.findall('window.__INITIAL_DATA__ =(.*?)</script>',
                                         requests.get(url='https://y.qq.com/n/ryqq/category',
                                                      headers=self._headers,
                                                      cookies=self._cookies).text)[0]).replace('undefined',
                                                                                               '"undefined"'))

    def get_lyrics(self, mid):  # 获取歌曲歌词信息
        return base64.b64decode(
            requests.get(url='https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg?_={}'
                             '&format=json&loginUin={}&songmid={}'.format(time.time(),
                                                                          ''.join(random.sample('1234567890', 10)),
                                                                          mid),
                         headers=self._headers, cookies=self._cookies).json()['lyric']).decode('utf-8')

    def get_radio_info(self):  # 获取个性电台信息
        return json.loads(str(re.findall('window.__INITIAL_DATA__ =(.*?)</script>',
                                         requests.get(url='https://y.qq.com/n/ryqq/radio',
                                                      headers=self._headers,
                                                      cookies=self._cookies).text)[0]).replace('undefined',
                                                                                               '"undefined"'))
