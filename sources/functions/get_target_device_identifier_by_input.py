import zipfile

import tqdm
import requests

import pygetwindow
import pickle
import paramiko
import os.path
import math
import ipdb
import importlib
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from telegram import Bot
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.encodings import Encoding
from os import path
from gtts import gTTS
from fastapi import HTTPException
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs


def get_target_identifier_by_input(input_ment, target_device_type):
    # todo 숫자 아니면 continue
    state_nick_name_passed = 0
    while 1:
        target_device_identifier_number = input(input_ment)
        target_device_identifier = f'{vpc_type}_#{target_device_identifier_number}'.lower()
        if 'no_#' or 'nx_#' or 'xc_#' or 'evm_#' in target_device_identifier:
            state_nick_name_passed = 1
        if state_nick_name_passed == 1:
            if LTA:
                logging.debug(f'''target_device_identifier={target_device_identifier} {'%%%FOO%%%' if LTA else ''}''')
            return target_device_identifier
