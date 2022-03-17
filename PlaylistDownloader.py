'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.03.16
Hosung.Kim
---------------------
Playlist Downloader Version 1.0.0
---------------------
Issues

* video downloading speed too slow
=====================
'''

from pytube import Playlist
from moviepy.editor import *

# playlistLink = "https://www.youtube.com/playlist?list=PLqCFQHCB2NpVjDwUQ6RvbI7BmUKZZKCgg"
# playlistLink = "https://youtube.com/playlist?list=PLqCFQHCB2NpUQzsMCPwyOgr96t40ZPd02"
playlistLink = input("Enter the link of the Youtube playlist you want to download.\n=>")

# DOWNLOAD_PATH = "/Users/kihoon.kim/Hosung/data/test/"
DOWNLOAD_PATH = input("Enter the path to save the Youtube videos.\n=>")

playlist = Playlist(playlistLink)

downloadStyle = input("Enter the download type. [video/audio]\n=>")

if input(f"Are you sure to download {playlist.title} into {downloadStyle}? [y/n]\n=>") not in 'Yy' :
    quit()

if downloadStyle == "audio" :
    for video in playlist.videos :
        FILE_NAME = video.title
        video.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first().download(DOWNLOAD_PATH, f"{FILE_NAME}.mp3")
elif downloadStyle == "video" :
    for video in playlist.videos :
        FILE_NAME = video.title

        video.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first().download(DOWNLOAD_PATH, f"{FILE_NAME}_video.mp4")
        video.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first().download(DOWNLOAD_PATH, f"{FILE_NAME}_audio.mp4")

        videoClip = VideoFileClip(f"{DOWNLOAD_PATH}{FILE_NAME}_video.mp4")
        audioClip = AudioFileClip(f"{DOWNLOAD_PATH}{FILE_NAME}_audio.mp4")

        videoClip.audio = audioClip

        videoClip.write_videofile(f"{DOWNLOAD_PATH}{FILE_NAME}.mp4")

        os.remove(f"{DOWNLOAD_PATH}{FILE_NAME}_video.mp4")
        os.remove(f"{DOWNLOAD_PATH}{FILE_NAME}_audio.mp4")
else :
    quit()

print(f"Youtube {downloadStyle} {playlist.title} is downloaded successfully.")

# count = 0
# data = ""
# for video in playlist.videos :
#     data += f"{video.title}\n"
#     video.streams.filter(only_audio=True).first().download(DOWNLOAD_PATH)
#     count += 1
#
# f = open("/Users/kihoon.kim/Hosung/data/document/playlistBackup.txt", "w")
# f.write(f"{count}\n{data}")
# f.close()
#
# Util.convertMP4toMP3(DOWNLOAD_PATH)