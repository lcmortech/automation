# Packages
# pip install yt-dlp
import yt-dlp
import json

#or

#import pytube
#import pytubefixA
#from pytube import YouTube
#URL  #ytlink
yt_vid = Youtube(URL)
yt_vid = yt_vid.streams.get_highest_resolution()
yt_vid.download()