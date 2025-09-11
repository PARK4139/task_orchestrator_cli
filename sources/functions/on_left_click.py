import yt_dlp

import webbrowser
import timeit
import threading
import requests
import pygetwindow
import json
import ipdb
import colorama
import chardet
from zipfile import BadZipFile
from typing import TypeVar, List
from seleniumbase import Driver
from selenium.webdriver.chrome.service import Service
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.ensure_console_cleared import ensure_console_cleared

from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING

from paramiko import SSHClient, AutoAddPolicy
from os import path
from functools import partial as functools_partial
from datetime import date
from cryptography.hazmat.backends import default_backend
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.get_pnxs import get_pnxs
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

import logging


def on_left_click(x, y, button, pressed):
    from pynput import mouse
    if pressed and button == mouse.Button.left:
        click_detected = True  # 클릭 감지 상태 업데이트
        logging.debug("마우스 왼쪽 클릭 감지됨!")
        return 0  # 마우스 왼쪽 클릭 감지되면 Listener 종료
