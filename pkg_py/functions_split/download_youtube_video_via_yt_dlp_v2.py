import webbrowser
import sys
import requests
import pythoncom
import pyautogui
import numpy as np
import mutagen
import math
import keyboard
import inspect
import datetime
import cv2
import colorama
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.state_via_context import SpeedControlContext
from moviepy import VideoFileClip
from bs4 import BeautifulSoup
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.functions_split.pk_print import pk_print


def download_youtube_video_via_yt_dlp_v2(D_FFMPEG_LOCATION, D_WORKING, ext, url):
    # from pkg_py.system_object.directories import D_WORKING
    #
    import yt_dlp
    import os

    ydl_opts = {
        'ffmpeg_location': D_FFMPEG_LOCATION,
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(D_WORKING, '%(title)s [%(id)s].%(ext)s'),
        'quiet': False,
        'noplaylist': True,
        'geo_bypass': True,
        'skip_unavailable_fragments': True,
        'fragment_retries': 5,
        # 'allow_unplayable_formats': False, # code for dev(debugging)
        'force_generic_extractor': True,
        'merge_output_format': ext,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        pk_print(f"downloading via ydl...   ({url})", print_color="blue")
        ydl.download([url])
