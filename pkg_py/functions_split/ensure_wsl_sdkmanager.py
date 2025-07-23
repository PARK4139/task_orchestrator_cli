import winreg
import traceback
import tomllib
import socket
import requests
import pygetwindow
import functools
import cv2
from zipfile import BadZipFile
from telegram import Bot
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from os.path import dirname
from functools import partial
from fastapi import HTTPException
from enum import Enum
from cryptography.hazmat.backends import default_backend
from pkg_py.pk_system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def ensure_wsl_sdkmanager(config_remote_os):
    # _______________________________________________________________________

    # [how] nvidia sdkmanager download.
    # nvidia developer login.
    # click button ".deb Ubuntu" # sdkmanager_2.2.0-12028_amd64.deb downloaded at 250331

    # wsl 에서 수행
    # ensure_general_ubuntu_pkg(ubuntu_pkg_n='sdkmanager', **config_remote_os) #
    cmd_to_remote_os(cmd='sudo apt update', **config_remote_os)
    cmd_to_remote_os(cmd='sudo apt --fix-broken install', **config_remote_os)
    # mv "/mnt/c/Autonomousa2z/Downloads/pk_working/sdkmanager_2.2.0-12028_amd64.deb" "."
    # explorer.exe .
    f_nx = 'sdkmanager_2.2.0-12028_amd64.deb'
    cmd_to_remote_os(cmd='mkdir -p ~/Downloads/pk_working', **config_remote_os)
    upload_pnx_to_remote_os(local_pnx_src=f'{D_DOWNLOADS}/pk_working/{f_nx}',
                            remote_pnx_dst=f'~/Downloads/pk_working/{f_nx}', **config_remote_os)
    cmd_to_remote_os(cmd=f'sudo dpkg -i ~/Downloads/pk_working/{f_nx}',
                     **config_remote_os)  # todo sdkmanager cli 로 업그레이드 시도
