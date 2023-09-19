from pytube import Playlist
import Util

playlistLink = input("Enter the link of the Youtube playlist you want to backup the list.\n=>")

DOWNLOAD_PATH = input("Enter the path to save the title list of playlist.\n=>")

playlist = Playlist(playlistLink)

if input(f"Are you sure to backup the title list of {playlist.title}? [y/n]\n=>") not in 'Yy' :
    quit()

playlistLen = playlist.length
count = 1
data = ""
for video in playlist.videos :
    data += f"{count}. {video.title}\n"
    count += 1
    Util.printProgressBar(count, playlistLen)

f = open(f"{DOWNLOAD_PATH}playlistBackup.txt", "w", encoding="UTF-8")
f.write(data)
f.close()

print(f"{playlist.title} backup process is finished successfully.")