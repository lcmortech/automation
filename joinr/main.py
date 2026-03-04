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
    ys = video.streams.get_highest_resolution().download(output_path="/joinr/playlists")
    ys.download()
    print(f"Downloaded: {video.title}")

#task
#set new dl dir ()
#increase quality of vid dls (text vid was lq)
#remove vid prev dled
