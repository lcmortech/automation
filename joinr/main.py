#import modules
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress

# get URL (test only short pl, save dir)
#penpot
url = input("https://www.youtube.com/playlist?list=PLqazFFzUAPc7g3Yw_0O3LqookKRnnfdZj")


# playlist
pl = Playlist(url)

#download playlist vid loop
for video in pl.videos:
    ys = video.streams.get_highest_resolution()
    ys.download()

#task
#set new dl dir
