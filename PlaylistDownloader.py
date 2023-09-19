'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.03.16
Hosung.Kim
---------------------
Issues

* video downloading speed too slow
=====================
'''

from pytube import Playlist
from moviepy.editor import *
import Util

playlistLink = input("Enter the link of the Youtube playlist you want to download.\n=>")

DOWNLOAD_PATH = input("Enter the path to save the Youtube videos.\n=>")

playlist = Playlist(playlistLink)

downloadStyle = input("Enter the download type. [video/audio]\n=>")

if input(f"Are you sure to download {playlist.title} into {downloadStyle}? [y/n]\n=>") not in 'Yy' :
    quit()

if downloadStyle == "audio" :
    # f = open("test22.txt", "r", encoding="UTF-8")
    count = 1
    length = len(str(len(playlist.videos)))
    for video in playlist.videos :
    # for i in range(200, len(playlist.videos)) :
        # video = playlist.videos[i]
        FILE_NAME = video.title
        # video.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first().download(DOWNLOAD_PATH, f"{str(count).zfill(length)}_{f.readline().strip()}.mp3")
        video.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first().download(DOWNLOAD_PATH, f"{FILE_NAME}.mp3")
        Util.printProgressBar(count, len(playlist.videos))
        count += 1
elif downloadStyle == "video" :
    for video in playlist.videos :
        count = 1
        FILE_NAME = video.title

        video.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first().download(DOWNLOAD_PATH, f"{FILE_NAME}_video.mp4")
        video.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first().download(DOWNLOAD_PATH, f"{FILE_NAME}_audio.mp4")

        videoClip = VideoFileClip(f"{DOWNLOAD_PATH}{FILE_NAME}_video.mp4")
        audioClip = AudioFileClip(f"{DOWNLOAD_PATH}{FILE_NAME}_audio.mp4")

        videoClip.audio = audioClip

        videoClip.write_videofile(f"{DOWNLOAD_PATH}{FILE_NAME}.mp4")

        os.remove(f"{DOWNLOAD_PATH}{FILE_NAME}_video.mp4")
        os.remove(f"{DOWNLOAD_PATH}{FILE_NAME}_audio.mp4")

        Util.printProgressBar(count, len(playlist.videos))
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