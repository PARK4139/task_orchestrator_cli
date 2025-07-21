import threading
import requests
import keyboard
import ipdb
from tkinter import UNDERLINE
from pytube import Playlist
from pynput import mouse
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE

from PIL import Image
from bs4 import ResultSet
from base64 import b64decode
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows

from pkg_py.simple_module.part_330_get_d_working import get_d_working


def do_random_schedules():
    import inspect
    import random
    func_n = inspect.currentframe().f_code.co_name
    int_random = random.randint(0, 7)
    # pk_system_Tts.speak(f'랜덤숫자 {int_random} 나왔습니다')
    # mkmk
    if int_random == 0:
        pass
    elif int_random == 1:
        pass
    elif int_random == 2:
        pass
    elif int_random == 3:
        pass
    elif int_random == 4:
        pass
    elif int_random == 5:
        pass
    elif int_random == 6:
        pass
    elif int_random == 7:
        pass
