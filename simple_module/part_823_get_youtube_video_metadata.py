import winreg
# import win32gui
import os.path
import mutagen
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_800_print_util import print_red


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
