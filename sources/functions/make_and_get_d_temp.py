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
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.pk_state_via_database import PkSqlite3DB
from os.path import dirname
from functools import partial as functools_partial
from fastapi import HTTPException
from cryptography.hazmat.primitives import padding
from Cryptodome.Cipher import AES
from bs4 import BeautifulSoup
from base64 import b64encode
from sources.functions.get_nx import get_nx
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided

from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging


def make_and_get_d_temp(prefix: str = "temp") -> str:
    # todo with open() 처럼 동작하는 코드로 만들어 보자 # pk_explorer # pk_dot_slash
    import uuid
    from pathlib import Path

    D_DESKTOP = Path.home() / "Desktop"
    unique_n = f"{prefix}_{uuid.uuid4().hex[:8]}"  # sample: temp_5f2d8c3a
    pnx_working = D_DESKTOP / unique_n

    if not is_pnx_existing(str(pnx_working)):
        ensure_pnx_made(pnx=str(pnx_working), mode='d')

    return str(pnx_working)
