import Main

QQM = Main.QQ_Music()
ret = QQM.get_toplist_music()
text = ''
for i in range(len(ret['toplistData']['song'])):
	text = text + '排名:{} 音乐名:{} 上升百分比:{} 歌手:{} music_id:{} mid:{}\n'.format(i + 1,
	                                                                        ret['toplistData']['song'][i]['title'],
	                                                                        ret['toplistData']['song'][i]['rankValue'],
	                                                                        ret['toplistData']['song'][i]['singerName'],
	                                                                        ret['toplistData']['song'][i]['songId'],
	                                                                        ret['toplistData']['song'][i]['albumMid'])
print('{}\n{}\n音乐信息:\n{}'.format(
	ret['toplistData']['titleShare'], ret['toplistData']['intro'], text))
