from pytube import Youtube
from sys import argv

def downloadYTVideo(link, folder = "\downloads"):
    ytvid = Youtube(link).streams.get_highest_resolution()
    ytvid.download(folder)
    

link = argv[1]

downloadYTVideo(link)
    