import winreg

import win32con
import tomllib
import threading
import tarfile
import socket
import shutil
import psutil
import os
import nest_asyncio
import importlib

import asyncio
from selenium.webdriver.support import expected_conditions as EC
from PySide6.QtWidgets import QApplication
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.get_list_calculated import get_list_calculated

from functools import partial as functools_partial
from functools import partial
from datetime import datetime
from bs4 import BeautifulSoup
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.get_pnxs import get_pnxs


def download_youtube_thumbnails_from_youtube_channel_main_page_url(youtube_channel_main_page_url):
    import os

    youtube_video_url_list = get_videos_urls_from_youtube_channel_main_page(
        youtube_channel_main_page_url=youtube_channel_main_page_url)
    channel_n = get_channel_n(channel_url=youtube_channel_main_page_url)
    d_dst = rf'{D_PK_WORKING_EXTERNAL}/thumbnails/{channel_n}'
    # dst = get_pnx_unix_style(pnx=dst)
    d_dst = get_pnx_os_style(pnx=d_dst)
    ensure_pnx_made(d_dst, mode="d")
    cnt = 0
    for youtube_video_url in youtube_video_url_list:
        cnt += 1
        f_jpg = os.path.join(d_dst, f"{channel_n}_thumbnail_maxresdefault_{cnt}.jpg")
        download_youtube_thumbnail(youtube_video_url=youtube_video_url, f_dst_jpg=f_jpg)
