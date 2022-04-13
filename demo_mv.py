import Main

QQM = Main.QQ_Music()
vid = 'r00127x0yzd'
data = QQM.get_mv_url(vid)
text = ''
for i in range(len(data['mvUrl']['data'][vid]['mp4'])):
	if data['mvUrl']['data'][vid]['mp4'][i]['filetype'] != 0:
		text = text + 'filetype:{} 大小:{} 下载URL:{}\n'.format(data['mvUrl']['data'][vid]['mp4'][i]['filetype'],
		                                                    data['mvUrl']['data'][vid]['mp4'][i]['fileSize'],
		                                                    data['mvUrl']['data'][vid]['mp4'][i][
			                                                    'freeflow_url'])
print('音乐名:{} 歌手:{}\n下载信息(filetype越高画质越高):\n{}'.format(data['mvInfo']['data'][vid]['name']
                                                       , data['mvInfo']['data'][vid]['singers'][0]['name'],
                                                       text))
