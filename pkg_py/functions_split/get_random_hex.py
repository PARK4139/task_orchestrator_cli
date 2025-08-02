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
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.map_massages import PkMessages2025
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from dirsync import sync
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def get_random_hex():
    import secrets

    return secrets.token_hex(16)  # 16바이트의 난수를 16진수 문자열로 생성
