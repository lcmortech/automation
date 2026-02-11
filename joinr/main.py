from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title:" + yt.title)
#get resolution
yt.streams.get_highest_resolution()
#check link
yt.download()

# Fixes:
# urllib error