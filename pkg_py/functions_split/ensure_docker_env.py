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
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.state_via_database import PkSqlite3DB
from PIL import Image
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnxs import get_pnxs


def ensure_docker_env():
    #
    import subprocess

    if not command_exists('docker'):
        ensure_printed('Docker missing: installing...', print_color='yellow')
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'docker.io'], check=True)
    else:
        ensure_printed('Docker exists')
    # 데몬 예외처리
    try:
        subprocess.run(['docker', 'info'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        ensure_printed('Docker daemon not running. Attempting to start...', print_color='yellow')
        # 시스템에 따라 service 또는 systemctl (WSL Ubuntu22.04는 systemctl, 18.04는 service)
        import platform
        start_cmd = ['sudo', 'service', 'docker', 'start']
        try:
            subprocess.run(start_cmd, check=True)
        except Exception as e:
            try:
                subprocess.run(['sudo', 'systemctl', 'start', 'docker'], check=True)
            except Exception as e2:
                ensure_printed(f'Docker daemon failed to start: {e}\n{e2}', print_color='red')
                raise RuntimeError("Docker daemon could not be started!")
        # 재확인
        try:
            subprocess.run(['docker', 'info'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            ensure_printed("Docker daemon started successfully.")
        except subprocess.CalledProcessError:
            ensure_printed("Docker daemon is still not running. Please check manually.", print_color="red")
            raise RuntimeError("Docker daemon is not running!")
    return ['docker']
