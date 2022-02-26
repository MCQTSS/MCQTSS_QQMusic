import Main

QQM = Main.QQ_Music()
QQM._cookies = QQM.set_cookie(cookie)  # Cookie获取方式readme.md有写
ret = QQM.get_playlist_info(7808278211)
playlist_name = ret['detail']['title']
playlist_desc = ret['detail']['desc']
playlist_host_nick = ret['detail']['host_nick']
print('歌单名:{} 歌单简介:{} 歌单作者:{}'.format(playlist_name, playlist_desc, playlist_host_nick))
tag = ''
for i in range(len(ret['detail']['tag'])):
    tag += ret['detail']['tag'][i]['name'] + ' '
print('歌单标签:{} 播放量:{} 收藏量:{}'.format(tag, ret['detail']['listennum'], ret['detail']['ordernum']))
print('*' * 50)
for i in range(len(ret['songList'])):
    mid = ret['songList'][i]['mid']
    music_id = ret['songList'][i]['id']
    name = ret['songList'][i]['name']
    album_mid = ret['songList'][i]['album']['mid']
    album_name = ret['songList'][i]['album']['name']
    singer = ret['songList'][i]['singer'][0]['name']
    print('歌曲名:{} ID:{} Mid:{} 专辑:{} 专辑Mid:{} 歌手:{}\n'.format(name, music_id, mid, album_name, album_mid, singer))
    print('*' * 50)
num = ret['detail']['songnum']
for j in range(int((num - 10) / 15 * 2)):
    ret = QQM.get_playlist_info_num(7808278211, j * 15 + 10)
    for i in range(len(ret['req_0']['data']['songlist'])):
        mid = ret['req_0']['data']['songlist'][i]['mid']
        music_id = ret['req_0']['data']['songlist'][i]['id']
        name = ret['req_0']['data']['songlist'][i]['name']
        album_mid = ret['req_0']['data']['songlist'][i]['album']['mid']
        album_name = ret['req_0']['data']['songlist'][i]['album']['name']
        singer = ret['req_0']['data']['songlist'][i]['singer'][0]['name']
        print('歌曲名:{} ID:{} Mid:{} 专辑:{} 专辑Mid:{} 歌手:{}\n'.format(name, music_id, mid, album_name, album_mid, singer))
        print('*' * 50)
