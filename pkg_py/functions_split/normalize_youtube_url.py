def normalize_youtube_url(url):
    """ YouTube URL을 표준 형식으로 변환 """
    if "youtube.com/watch?v=" in url and "youtu.be" in url:
        url = url.replace("https://www.youtube.com/watch?v=https://youtu.be/", "https://youtu.be/")

    # youtu.be 형식의 단축 URL을 표준 watch?v= 형식으로 변환
    if "youtu.be/" in url:
        video_id = url.split("youtu.be/")[-1].split("?")[0]  # YouTube 영상 ID 추출
        url = f"https://www.youtube.com/watch?v={video_id}"

    return url
