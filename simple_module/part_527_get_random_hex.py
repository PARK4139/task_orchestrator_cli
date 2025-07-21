import zlib
import urllib.parse
import string
import socket
import re
import pythoncom
import paramiko
import os.path
import os
import nest_asyncio
import math
import datetime
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from dirsync import sync
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from base64 import b64encode
from base64 import b64decode
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def get_random_hex():
    import secrets

    return secrets.token_hex(16)  # 16바이트의 난수를 16진수 문자열로 생성
