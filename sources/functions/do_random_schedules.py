import threading
import requests
import keyboard
import ipdb
from tkinter import UNDERLINE
from pytube import Playlist
from pynput import mouse
from sources.functions.get_historical_list import get_historical_list
from sources.functions.does_pnx_exist import is_pnx_existing
import logging
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER

from PIL import Image
from bs4 import ResultSet
from base64 import b64decode
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows

from sources.functions.get_d_working import get_d_working


def do_random_schedules():
    import inspect
    import random
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    int_random = random.randint(0, 7)
    # task_orchestrator_cli_Tts.speak(f'랜덤숫자 {int_random} 나왔습니다')
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
