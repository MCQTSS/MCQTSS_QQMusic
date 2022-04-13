import Main

QQM = Main.QQ_Music()
QQM._cookies = QQM.set_cookie(cookie)  # Cookie获取方式readme.md有写
list_search = QQM.search_music('周杰伦', 20)
for i in range(len(list_search)):
    mid = list_search[i]['mid']
    music_id = list_search[i]['id']
    name = list_search[i]['name']
    album_mid = list_search[i]['album']['mid']
    album_name = list_search[i]['album']['name']
    singer = list_search[i]['singer'][0]['name']
    vid = list_search[i]['mv']['vid']
	print(
		'歌曲名:{} ID:{} Mid:{} 专辑:{} 专辑Mid:{} 歌手:{} 歌曲MVVid:{}'.format(name, music_id, mid, album_name, album_mid, singer,
		                                                             vid))
    print('*' * 50)
# print(QQM.get_music_info(list_search[0]['id']))  # 通过音乐ID来获取音乐信息(和搜索获取的感觉差不多)
album_info = QQM.get_album_info(list_search[0]['album']['mid'])
print(album_info)
print('歌曲{}的专辑信息:\n'
      '专辑名:{} 发行时间:{} 发行公司:{} 专辑语言:{} 专辑类型:{} 专辑类型:{}\n'
      '专辑介绍:{}\n'
      '专辑发行公司介绍:{}'.format(list_search[0]['name'],
                           album_info['req_1']['data']['basicInfo']['albumName'],
                           album_info['req_1']['data']['basicInfo']['publishDate'],
                           album_info['req_1']['data']['company']['name'],
                           album_info['req_1']['data']['basicInfo']['language'],
                           album_info['req_1']['data']['basicInfo']['genre'],
                           album_info['req_1']['data']['basicInfo']['albumType'],
                           album_info['req_1']['data']['basicInfo']['desc'],
                           album_info['req_1']['data']['company']['brief']))
music_url = QQM.get_music_url(list_search[0]['mid'])
print('音乐播放URL:', music_url)
print('音乐歌词:\n{}'.format(QQM.get_lyrics(list_search[0]['mid'])))
print(QQM.get_radio_info())
