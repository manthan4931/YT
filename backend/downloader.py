from config import *
import os 
import yt_dlp
def download_mp3(url:str):
    os.makedirs(download_dir,exist_ok=True)


    ydl_opts={
        'format':'bestaudio/best/best',
        'outtmpl':f'{download_dir}/%(title)s.%(ext)s',
        'cookiefile':'cookies.txt',
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':audio_quality,
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info=ydl.extract_info(url,download=True)
        filename=ydl.prepare_filename(info)
    mp3_filename=filename.rsplit(".",1)[0]+".mp3"
    return mp3_filename