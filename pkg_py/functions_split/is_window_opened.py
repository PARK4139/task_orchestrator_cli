import zipfile
import yt_dlp
import win32con
import tqdm
import timeit
import platform
from selenium.webdriver.support import expected_conditions as EC
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.directories import D_PKG_TXT, D_PK_WORKING
from pkg_py.system_object.local_test_activate import LTA
from pathlib import Path
from datetime import datetime
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA


def is_window_opened(window_title_seg):
    windows_titles_opened = get_windows_opened()
    windows_titles_opened = get_list_without_none(working_list=windows_titles_opened)

    # print_list_as_vertical(working_list=windows_titles_opened,working_list_n="windows_titles_opened")

    for windows_title_opened in windows_titles_opened:
        if window_title_seg in windows_title_opened:
            # ensure_printed(f'''{windows_title_opened}" 창이 열려 있습니다''')
            return 1
    # ensure_printed(f'''{window_title_seg}" 창이 닫혀 있습니다''')
    return 0
