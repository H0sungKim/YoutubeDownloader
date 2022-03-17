'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.03.16
Hosung.Kim
---------------------
Playlist Downloader TestVersion
---------------------
Issues

* video download
=====================
'''

from pytube import Playlist
import Util

# playlistLink = "https://www.youtube.com/playlist?list=PLqCFQHCB2NpVjDwUQ6RvbI7BmUKZZKCgg"
# playlistLink = "https://youtube.com/playlist?list=PLqCFQHCB2NpUQzsMCPwyOgr96t40ZPd02"
playlistLink = input("Enter the link of the Youtube playlist you want to download.\n=>")

# DOWNLOAD_PATH = "/Users/kihoon.kim/Hosung/data/document/"
DOWNLOAD_PATH = input("Enter the path to save the Youtube videos.\n=>")

playlist = Playlist(playlistLink)

downloadStyle = input("Enter the download type. [video/audio]\n=>")

if input(f"Are you sure to download {playlist.title} into {downloadStyle}? [y/n]\n=>") not in 'Yy' :
    quit()

if downloadStyle == "audio" :
    for video in playlist.videos :
        video.streams.filter(only_audio=True).first().download(DOWNLOAD_PATH)
    Util.convertMP4toMP3(DOWNLOAD_PATH)
elif downloadStyle == "video" :
    pass
else :
    quit()

print(f"Youtube {downloadStyle} {playlist.title} is downloaded successfully.")

# # DOWNLOAD_PATH = input("Enter the path to save the Youtube video.\n=>")
#
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