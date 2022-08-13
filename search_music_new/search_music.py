import execjs
import requests
import json
import time
import random

rFile = open("./getsearchid.js", 'r', encoding='UTF-8')
sid = execjs.compile(rFile.read()).call('l', '3')
print(sid)
data = json.dumps({"comm": {"g_tk": 997034911, "uin": ''.join(random.sample('1234567890', 10)), "format": "json",
                            "inCharset": "utf-8",
                            "outCharset": "utf-8", "notice": 0, "platform": "h5", "needNewCode": 1, "ct": 23, "cv": 0},
                   "req_0": {"method": "DoSearchForQQMusicDesktop", "module": "music.search.SearchCgiService",
                             "param": {"remoteplace": "txt.mqq.all", "searchid": sid, "search_type": 0,
                                       "query": input("请输入要搜索的音乐名:"), "page_num": 1, "num_per_page": 20}}},
                  ensure_ascii=False).encode('utf-8')
resp = requests.post(
	url='https://u.y.qq.com/cgi-bin/musicu.fcg?_webcgikey=DoSearchForQQMusicDesktop&_={}'.format(
		int(round(time.time() * 1000))),
	headers={
		'Accept': '*/*',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
		'Referer': 'https://y.qq.com/',
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 ('
		              'KHTML, like Gecko) Mobile/17D50 UCBrowser/12.8.2.1268 Mobile AliApp(TUnionSDK/0.1.20.3) '},
	data=data)
print(resp.json())
rFile.close()
