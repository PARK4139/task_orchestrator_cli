import winreg

import tomllib
import sys
import socket
import re
import pywintypes

import pyglet
import os.path
import importlib
from tkinter import UNDERLINE
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX


from sources.objects.pk_local_test_activate import LTA
from moviepy import VideoFileClip
from gtts import gTTS
from datetime import timedelta
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from sources.functions.get_pnx_unix_style import get_pnx_unix_style

from sources.functions.get_d_working import get_d_working


def get_modified_f_list(previous_state, current_state):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    return DataStructureUtil.get_different_elements(list1=current_state, list2=previous_state)
