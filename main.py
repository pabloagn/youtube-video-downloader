import os
import yt_dlp as youtube_dl
from logger import logger

def get_video_resolution(info_dict):
    formats = info_dict.get('formats', [])
    video_format = next((f for f in formats if f['vcodec'] != 'none' and f['acodec'] == 'none'), None)
    if video_format:
        width = video_format.get('width')
        height = video_format.get('height')
        return f"{width}x{height}" if width and height else "Resolution info not available"
    return "Resolution info not available"

def download_video(url, download_path, cookies_path):
    logger.info(f"Starting download for video: {url}")
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'cookies': cookies_path,
        'merge_output_format': 'mkv',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mkv',
        }],
        'quiet': True,
        'no_warnings': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get('title', None)
        final_resolution = get_video_resolution(info_dict)
        logger.info(f"Downloaded and merged: {video_title}")
        logger.info(f"Final resolution: {final_resolution}")

def download_playlist(playlist_url, download_path, cookies_path):
    logger.info(f"Starting download for playlist: {playlist_url}")
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'cookies': cookies_path,
        'merge_output_format': 'mkv',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mkv',
        }],
        'quiet': True,
        'no_warnings': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def main(operation_mode: str,
         inputs_path: str,
         download_path: str,
         cookies_path: str):
    '''
    Execute YouTube video downloading based on parameters.
    '''
    logger.info("Main function started")
    if not os.path.exists(download_path):
        os.makedirs(download_path)
        logger.info(f"Created download path: {download_path}")

    if operation_mode == "V":
        if os.path.exists('videos.txt'):
            logger.info("videos.txt found")
            with open('videos.txt', 'r') as file:
                video_urls = file.readlines()
                for url in video_urls:
                    logger.info(f"Processing video URL: {url.strip()}")
                    download_video(url.strip(), download_path, cookies_path)
        else:
            logger.warning("videos.txt not found")

    elif operation_mode == "P":
        if os.path.exists('playlists.txt'):
            logger.info("playlists.txt found")
            with open('playlists.txt', 'r') as file:
                playlist_urls = file.readlines()
                for url in playlist_urls:
                    logger.info(f"Processing playlist URL: {url.strip()}")
                    download_playlist(url.strip(), download_path, cookies_path)
        else:
            logger.warning("playlists.txt not found")

if __name__ == "__main__":
    operation_mode = "P"
    download_path = "D:\\Downloads"
    cookies_path = "D:\\Downloads\\cookies.txt"
    main(operation_mode, download_path, cookies_path)