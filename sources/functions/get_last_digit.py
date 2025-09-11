import win32con
import toml
import toml
import timeit
import random
import cv2
import colorama
import clipboard
from urllib.parse import quote
from selenium.webdriver.chrome.service import Service
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from sources.functions.ensure_window_to_front import ensure_window_to_front
import logging
from sources.objects.pk_etc import PkFilter

from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI


from PIL import Image
from os import path
from functools import partial as functools_partial
from datetime import timedelta
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
from sources.functions.get_d_working import get_d_working


def get_last_digit(prompt):
    # todo : get_front_digit() 도 만드는 게 좋겠다.
    import inspect
    import re

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    match = re.search(r'\d+\b$', prompt.strip())  # 끝에 위치한 모든 연속된 숫자를 찾음
    if match:
        return match.group(0)  # 매칭된 숫자 반환
    return "00"  # 숫자를 찾지 못한 경우 기본값 "00" 반환
