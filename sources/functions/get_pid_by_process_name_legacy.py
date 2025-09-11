import shutil
import requests
import re

import importlib
import datetime
import calendar
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist


from sources.functions.get_d_working import get_d_working
import logging
from sources.functions.get_list_sorted import get_list_sorted

from pathlib import Path
from Cryptodome.Cipher import AES
from base64 import b64decode
from sources.functions.ensure_value_completed import ensure_value_completed

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style


def get_pid_by_process_name_legacy(process_name: str):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    # Q.how to activate certain program window at python?
    pids: str = get_all_pid_and_process_name()
    # debug_as_gui(f"pids:\n\n{pids}")
    pids: list[str] = [i for i in pids.split("\n") if
                       is_pattern_in_prompt(prompt=i, pattern=process_name)]  # 프로세스명이 target_process_name 인 경우만 추출
    pids: str = pids[0].split(",")[1].replace("pid:",
                                              "").strip()  # strip() 은 특정 문자를 remove를 위해서 만들어짐. 단어를 remove하기 위해서는 replace() 가 더 적절하다고 chatGPT 는 말한다.
    target_pid = int(pids)  # 추출된 target_process_name 의 pid
    print_as_gui(f"target_process_name 프로세스 정보\n\n{target_pid}")
    return target_pid
