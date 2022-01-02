'''
YoutubeVideoDownloader by Kevin Flynn (xars7)
Started: 1-2-22

Description -- This program is designed to download YouTube videos from the internet via 
                URL. 
'''

# import os and pytube module
import os
from pytube import YouTube

# set the path 
user_profile = os.path.expanduser('~')
user_desktop = user_profile + "/Desktop"
SAVE_PATH = user_desktop + "/YouTubeVideoDownloader"

# set the download link 
# example link to someordinarygamers :) "https://www.youtube.com/watch?v=3cZKNPUx3pA"
link = input("Please enter the url of the video you would like to download: ")

# download the video 
yt = YouTube(link)
stream = yt.streams.filter(file_extension='mp4').first()
stream.download(SAVE_PATH)