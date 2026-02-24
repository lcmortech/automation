#import modules
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress

# get URL
url = input("Input Youtube Playlist URL")

# playlist
pl = Playlist(url)

for video in pl.videos:
    pass

