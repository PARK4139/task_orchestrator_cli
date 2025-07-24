

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
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_press import pk_press

from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.directories import D_WORKING
from pkg_py.system_object.directories import D_PKG_TXT
from pkg_py.system_object.state_via_database import PkSqlite3DB
from passlib.context import CryptContext
from os import path
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style


def download_remote_release_n_n_n_zip_via_scp(vpc_aifw_version, dst):
    # def send_src_to_remote_os(src, port, users, ip, pw):
    dst = get_pnx_windows_style(dst)
    user_gitlab_token = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\user_gitlab_token.txt', initial_str="")
    ip_gitlab_token = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\ip_gitlab_token.txt', initial_str="")
    pw_gitlab_token = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\pw_gitlab_token.txt', initial_str="")
    port_gitlab_token = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\port_gitlab_token.txt', initial_str="")
    src = rf'{user_gitlab_token}@{ip_gitlab_token}:/home/user/release/remote_release_{vpc_aifw_version}.zip'
    cmd = rf"scp -P {port_gitlab_token} -r {src} {dst}"
    # cmd_to_os(cmd=cmd) # warning : pw 물은 채로 정지
    cmd_to_os_like_person(cmd=cmd)  # warning : pw 물은 채로 정지
    window_title_seg = r"C:\Windows\system32\cmd"
    while 1:
        pk_sleep(milliseconds=2000)
        if is_window_opened(window_title_seg=window_title_seg):
            ensure_window_to_front(window_title_seg=window_title_seg)
            pk_sleep(milliseconds=500)  # success : 중요.
            write_like_person(str_working=pw_gitlab_token)
            pk_press("enter")
            break
    pk_sleep(milliseconds=500)
