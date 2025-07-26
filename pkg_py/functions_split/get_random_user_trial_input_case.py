import win32con
import traceback
import tqdm
import string
import pyautogui
import pickle
import nest_asyncio

from yt_dlp import YoutubeDL
from pytube import Playlist
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.press import press
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from os import path
from fastapi import HTTPException
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style


def get_random_user_trial_input_case():
    import random
    import string

    options = [
        get_random_korean_name(),
        get_random_korean_phone_number(),
        get_random_id(30),
        get_random_special_character(30),
        string.punctuation,
        get_random_special_character(30),
        # get_random_hex(),
        # get_random_bytes(),
        get_random_date(),
        "None",
        None,
        ""
    ]
    return random.choice(options)
