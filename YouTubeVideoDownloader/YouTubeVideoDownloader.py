'''
YoutubeVideoDownloader by Kevin Flynn (xars7)
Started: 1-2-22

Description -- This program is designed to download YouTube videos from the internet via 
                URL. 
'''

from pytube import YouTube

SAVE_PATH = "/home/xars7/Desktop"

link = "https://www.youtube.com/watch?v=3cZKNPUx3pA"

yt = YouTube(link)
stream = yt.streams.first()
stream.download(SAVE_PATH)