#import modules
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
from moviepy import *
# get URL (test only short pl, save dir)
#penpot
url = input("https://www.youtube.com/playlist?list=PLqazFFzUAPc7g3Yw_0O3LqookKRnnfdZj")


# playlist
pl = Playlist(url)

#download playlist vid loop
for video in pl.videos:
    ys = video.streams.get_highest_resolution().download(output_path="/joinr/playlists")
    ys.download()
    print(f"Downloaded: {video.title}")

clip = VideoFileClip("vid")

#task
#set new dl dir ()gi
#increase quality of vid dls (text vid was lq)
#remove vid prev dled - complete
# adjust quality of new vid dl - incomplete
# exit .venv
# pull test - complete
# moviepy docs (join playlist)
# add queue variable for clips (if queue then merge with clip at index 0 of queue - while que's index is more than 0?)