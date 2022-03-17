import os

def convertMP4toMP3(path) :
    fileList = os.listdir(path)

    for file in fileList :
        if '.mp4' in file :
            os.rename(path + file, path + file.replace('.mp4', '.mp3'))

def simplifyTitle(title) :
    # Erik Satie : "Je Te Veux"  =>  Je Te Veux
    title = title.split(":")[1]
    return title.replace("\"", "").strip()
