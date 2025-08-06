from torch.fx.experimental.symbolic_shapes import lru_cache


@lru_cache(maxsize=1)
def ensure_ffmpeg_installed_to_pkg_windows():
    from pkg_py.system_object.directories import D_PKG_WINDOWS

    import os
    import zipfile
    import urllib.request
    import shutil
    import traceback
    from pkg_py.functions_split.ensure_printed import ensure_printed

    ffmpeg_exe_path = os.path.join(D_PKG_WINDOWS, "ffmpeg.exe")
    ffprobe_exe_path = os.path.join(D_PKG_WINDOWS, "ffprobe.exe")

    # 둘 다 있으면 바로 반환
    if os.path.exists(ffmpeg_exe_path) and os.path.exists(ffprobe_exe_path):
        ensure_printed(f"[FFMPEG]  ffmpeg.exe 및 ffprobe.exe 이미 설치됨", print_color="green")
        return ffmpeg_exe_path, ffprobe_exe_path

    # 설치 시작
    ensure_printed(f"[FFMPEG]  설치 시작", print_color="cyan")
    os.makedirs(D_PKG_WINDOWS, exist_ok=True)

    try:
        zip_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        temp_zip = os.path.join(D_PKG_WINDOWS, "ffmpeg_temp.zip")
        extract_dir = os.path.join(D_PKG_WINDOWS, "extracted_ffmpeg")

        ensure_printed(f"[FFMPEG]  다운로드 중: {zip_url}", print_color="cyan")
        urllib.request.urlretrieve(zip_url, temp_zip)
        ensure_printed(f"[FFMPEG]  다운로드 완료: {temp_zip}", print_color="cyan")

        with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        ensure_printed(f"[FFMPEG]  압축 해제 완료: {extract_dir}", print_color="cyan")

        found = False
        for root, dirs, files in os.walk(extract_dir):
            if "ffmpeg.exe" in files and "ffprobe.exe" in files:
                shutil.copy2(os.path.join(root, "ffmpeg.exe"), ffmpeg_exe_path)
                shutil.copy2(os.path.join(root, "ffprobe.exe"), ffprobe_exe_path)
                ensure_printed(f"[FFMPEG]  ffmpeg.exe, ffprobe.exe 복사 완료", print_color="green")
                found = True
                break

        os.remove(temp_zip)
        shutil.rmtree(extract_dir, ignore_errors=True)

        if not found:
            raise FileNotFoundError("ffmpeg.exe 또는 ffprobe.exe를 찾을 수 없습니다.")

        return ffmpeg_exe_path, ffprobe_exe_path

    except Exception as e:
        ensure_printed(f"[FFMPEG]  설치 실패: {e}", print_color="red")
        traceback.print_exc()
        return None, None
