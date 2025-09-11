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
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.ensure_pressed import ensure_pressed
import logging

from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.pk_map_texts import PkTexts

from sources.objects.pk_local_test_activate import LTA
from dirsync import sync
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from base64 import b64encode
from base64 import b64decode
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.is_f import is_f
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def get_random_hex():
    import secrets

    return secrets.token_hex(16)  # 16바이트의 난수를 16진수 문자열로 생성
