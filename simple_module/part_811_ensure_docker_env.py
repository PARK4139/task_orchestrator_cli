import uuid
import tomllib
import tarfile
import sys
import sqlite3
import shutil
import paramiko
import numpy as np
import mutagen
import keyboard
import ipdb
import datetime
from zipfile import BadZipFile
from urllib.parse import urlparse
from selenium.common.exceptions import ElementClickInterceptedException
from PySide6.QtWidgets import QApplication
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from PIL import Image
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def ensure_docker_env():
    #
    import subprocess

    if not command_exists('docker'):
        pk_print('Docker missing: installing...', print_color='yellow')
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'docker.io'], check=True)
    else:
        pk_print('Docker exists')
    # 데몬 예외처리
    try:
        subprocess.run(['docker', 'info'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        pk_print('Docker daemon not running. Attempting to start...', print_color='yellow')
        # 시스템에 따라 service 또는 systemctl (WSL Ubuntu22.04는 systemctl, 18.04는 service)
        import platform
        start_cmd = ['sudo', 'service', 'docker', 'start']
        try:
            subprocess.run(start_cmd, check=True)
        except Exception as e:
            try:
                subprocess.run(['sudo', 'systemctl', 'start', 'docker'], check=True)
            except Exception as e2:
                pk_print(f'Docker daemon failed to start: {e}\n{e2}', print_color='red')
                raise RuntimeError("Docker daemon could not be started!")
        # 재확인
        try:
            subprocess.run(['docker', 'info'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            pk_print("Docker daemon started successfully.")
        except subprocess.CalledProcessError:
            pk_print("Docker daemon is still not running. Please check manually.", print_color="red")
            raise RuntimeError("Docker daemon is not running!")
    return ['docker']
