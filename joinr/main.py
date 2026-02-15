from pytube import YouTube
#from sys import argv

#from docs
yt = YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0')

print("Title:" + yt.title)
#get resolution
yt.streams.get_highest_resolution()
#check link
yt.download()

# Bugs:
# urllib error
# check api (corey schafer for tips)
# check pip
# not sure. might retype code tomorrow