import urllib
import toml
import requests
import random
import pygetwindow
import nest_asyncio
import colorama
import browser_cookie3
from yt_dlp import YoutubeDL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated
from PIL import Image
from enum import Enum
from Cryptodome.Cipher import AES
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def xcopy_with_overwrite(pnx, pnx_future):
    import inspect
    import subprocess
    import traceback

    func_n = inspect.currentframe().f_code.co_name
    try:
        result = cmd_to_os_like_person_as_admin(rf'echo a | xcopy "{pnx}" "{pnx_future}" /e /h /k /y')
        if result == subprocess.CalledProcessError:
            if is_f(pnx):
                cmd_to_os_like_person_as_admin(rf'echo f | xcopy "{pnx}" "{pnx_future}" /e /h /k /y')
            else:
                cmd_to_os_like_person_as_admin(rf'echo d | xcopy "{pnx}" "{pnx_future}" /e /h /k /y')
    except Exception:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
