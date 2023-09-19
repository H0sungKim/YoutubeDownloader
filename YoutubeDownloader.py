'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.03.15
Hosung.Kim
---------------------
Issues

* video downloading speed too slow
=====================
'''

from pytube import YouTube
from moviepy.editor import *
import os

videoLink = input("Enter the link of the Youtube video you want to download.\n=>")

DOWNLOAD_PATH = input("Enter the path to save the Youtube video.\n=>")

youtube = YouTube(videoLink, use_oauth=False, allow_oauth_cache=True)
FILE_NAME = youtube.title

downloadStyle = input("Enter the download type. [video/audio]\n=>")

if input(f"Are you sure to download {youtube.title} into {downloadStyle}? [y/n]\n=>") not in 'Yy' :
    quit()

if downloadStyle == "audio" :
    youtube.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first().download(DOWNLOAD_PATH, f"{FILE_NAME}.mp3")
    # youtube.streams.filter(only_audio=True).first().download(DOWNLOAD_PATH)

elif downloadStyle == "video" :
    youtube.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first().download(DOWNLOAD_PATH, f"{FILE_NAME}_video.mp4")
    youtube.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first().download(DOWNLOAD_PATH, f"{FILE_NAME}_audio.mp4")
    

    videoClip = VideoFileClip(f"{DOWNLOAD_PATH}{FILE_NAME}_video.mp4")
    audioClip = AudioFileClip(f"{DOWNLOAD_PATH}{FILE_NAME}_audio.mp4")

    videoClip.audio = audioClip

    videoClip.write_videofile(f"{DOWNLOAD_PATH}{FILE_NAME}.mp4")

    os.remove(f"{DOWNLOAD_PATH}{FILE_NAME}_video.mp4")
    os.remove(f"{DOWNLOAD_PATH}{FILE_NAME}_audio.mp4")
    # youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

else :
    quit()

print(f"Youtube {downloadStyle} {FILE_NAME} is downloaded successfully.")

# count = 0
# data = ""
# for video in playlist.videos :
#     data += f"{video.title}\n"
#     count += 1

# f = open("/Users/kihoon.kim/Hosung/data/document/playlistBackup.txt", "w")
# f.write(f"{count}\n{data}")
# f.close()

# youtube.streams.get_by_itag(140).download()
# print(youtube.streams.filter(only_audio=True).all())

# print(youtube.title)