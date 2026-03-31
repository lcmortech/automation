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

# check directory
clip = VideoFileClip("directory")

#loop to merge vids

#task
#set new dl dir ()gi
#increase quality of vid dls (text vid was lq)
#remove vid prev dled - complete
# adjust quality of new vid dl - incomplete
# moviepy docs (join playlist)
# deactivate (.venv)
# final_clip = concatenate_videoclips([clip1, clip2, clip3])
# final_clip.write_videofile("newVideo.mp4", codec="libx264")
# look into diff codecs (might improve dl quality)
# add queue variable for clips (if queue then merge with clip at index 0 of queue - while que's index is more than 0?)
# add gui (tkinter)
# tkinter docs - https://docs.python.org/3/library/tkinter.html
# add unit tests to both modules (pytest)
# hospital stay - 3/18
# home recovery - 3/19
# home recovery - 3/20
# add ffmpeg to improve dl quality
# still recovering (anemia nausea)
# recovering still (still nausea)
# taking break (again)
# still recovering 
# sick again (a cold this time)
# actually flu (and fever)
# still sick (flu gone)
