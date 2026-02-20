# from pytube import YouTube
# #from sys import argv

# #from docs
# yt = YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0')

# print("Title:" + yt.title)
# #get resolution

# print(yt.description)
# desc = yt.description
# length = yt.length
# yt.streams.get_highest_resolution()
# #check link
# yt.download()

# # Bugs:
# # urllib error
# # check api (corey schafer for tips)

from pytubefix import YouTube
from pytubefix.cli import on_progress


#gangnam style
url = "https://www.youtube.com/watch?v=9bZkp7q19f0"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()

#bug
# fix pytube cli error 
# https://pytubefix.readthedocs.io/en/latest/
# 2-18 success!