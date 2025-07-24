import webbrowser
import uuid
import threading
import tarfile
import sys
import speech_recognition as sr
import requests

import pythoncom
import pyautogui
import psutil
import os
import nest_asyncio
import ipdb
import inspect
import functools
import colorama
from zipfile import BadZipFile
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.state_via_database import PkSqlite3DB
from os.path import dirname
from functools import partial as functools_partial
from fastapi import HTTPException
from cryptography.hazmat.primitives import padding
from Cryptodome.Cipher import AES
from bs4 import BeautifulSoup
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def make_and_get_d_temp(prefix: str = "temp") -> str:
    # todo with open() 처럼 동작하는 코드로 만들어 보자 # pk_explorer # pk_dot_slash
    import uuid
    from pathlib import Path

    D_DESKTOP = Path.home() / "Desktop"
    unique_n = f"{prefix}_{uuid.uuid4().hex[:8]}"  # sample: temp_5f2d8c3a
    pnx_working = D_DESKTOP / unique_n

    if not does_pnx_exist(str(pnx_working)):
        ensure_pnx_made(pnx=str(pnx_working), mode='d')

    return str(pnx_working)
