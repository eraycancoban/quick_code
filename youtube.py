import string
import pytube
import tkinter as tk
from pytube import YouTube
from pytube.cli import on_progress


#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link, on_progress_callback=on_progress)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")




