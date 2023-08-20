import subprocess
import re

def get_filename(video_url):
    filename = re.search(r"rutube\.ru\/(.+?)\/", video_url).group(1)
    return filename

def get_video_info(video_url):
    ffmpeg_cmd = ['ffmpeg', '-i', video_url]
    subprocess.run(ffmpeg_cmd)

    download_option = input("Хотите скачать видео? (да/нет): ")
    if download_option.lower() == 'да':
        filename = get_filename(video_url)
        download_video(video_url, filename)

def download_video(video_url, filename):
    ffmpeg_cmd = ['ffmpeg', '-i', video_url, '-c', 'copy', filename + '.mp4']
    subprocess.run(ffmpeg_cmd)

video_url = input("Введите URL видео: ")
get_video_info(video_url)