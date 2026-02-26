#import modules
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress

# get URL (test only short pl, save dir)
url = input("Input Youtube Playlist URL")

# playlist
pl = Playlist(url)

#download playlist vid loop
for video in pl.videos:
    ys = video.streams.get_highest_resolution()
    ys.download()

