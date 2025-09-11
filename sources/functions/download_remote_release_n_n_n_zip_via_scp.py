

import zlib
import zipfile
import subprocess
import pyautogui
import pyaudio
import functools
import calendar
from zipfile import BadZipFile
from selenium.webdriver.support import expected_conditions as EC
from prompt_toolkit.styles import Style

from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed

from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f

from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.pk_state_via_database import PkSqlite3DB
from passlib.context import CryptContext
from os import path
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_windows_style import get_pnx_windows_style


def download_remote_release_n_n_n_zip_via_scp(vpc_aifw_version, dst):
    # def send_src_to_remote_os(src, port, users, ip, pw):
    dst = get_pnx_windows_style(dst)
    user_gitlab_token = get_token_from_f_token(f_token=rf'{D_PK_RECYCLE_BIN}\user_gitlab_token.txt', initial_str="")
    ip_gitlab_token = get_token_from_f_token(f_token=rf'{D_PK_RECYCLE_BIN}\ip_gitlab_token.txt', initial_str="")
    pw_gitlab_token = get_token_from_f_token(f_token=rf'{D_PK_RECYCLE_BIN}\pw_gitlab_token.txt', initial_str="")
    port_gitlab_token = get_token_from_f_token(f_token=rf'{D_PK_RECYCLE_BIN}\port_gitlab_token.txt', initial_str="")
    src = rf'{user_gitlab_token}@{ip_gitlab_token}:/home/user/release/remote_release_{vpc_aifw_version}.zip'
    cmd = rf"scp -P {port_gitlab_token} -r {src} {dst}"
    # ensure_command_executed(cmd=cmd) # warning : pw 물은 채로 정지
    ensure_command_executed_like_human(cmd=cmd)  # warning : pw 물은 채로 정지
    window_title_seg = r"C:\Windows\system32\cmd"
    while 1:
        ensure_slept(milliseconds=2000)
        if is_window_opened(window_title_seg=window_title_seg):
            ensure_window_to_front(window_title_seg)
            ensure_slept(milliseconds=500)  # success : 중요.
            ensure_writen_like_human(str_working=pw_gitlab_token)
            ensure_pressed("enter")
            break
    ensure_slept(milliseconds=500)
