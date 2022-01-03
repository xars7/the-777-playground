'''
YoutubeVideoDownloader by Kevin Flynn (xars7)
Started: 1-2-22

Description -- This program is designed to download YouTube videos from the internet via 
                URL and store them in a folder on your Desktop. 

*** NOTE: this program uses the module pytube. In order to run this program on your 
          own computer you need to install it using pip. Please refer to the ReadMe inside of
          this project to learn how to install it

          if you are interested in using pytube in your next project I strongly suggest 
          you head to their website and read their documentation it is super simple and
          easy to digest
          
          Link to pytube's webpage: https://pytube.io/en/latest/index.html
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