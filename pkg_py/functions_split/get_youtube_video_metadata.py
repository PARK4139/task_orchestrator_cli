


def get_youtube_video_metadata(yt_dlp, url):
    ydl_extract_opts = {
        'quiet': True,
        'skip_download': True
    }
    with yt_dlp.YoutubeDL(ydl_extract_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info.get("title")
        clip_id = info.get("id")
        ext = info.get("ext", "mp4")
    return info, title, clip_id, ext
