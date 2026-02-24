#import modules
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress

url = input("Input Youtube Playlist URL")

p = Playlist(url)