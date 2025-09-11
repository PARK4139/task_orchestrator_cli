import yt_dlp

import win32con
import timeit
import tarfile
import sys
import requests
import random
import pythoncom
import pyautogui
import paramiko
import pandas as pd
import os.path
import os, inspect
import numpy as np
import nest_asyncio
import math
import clipboard
import chardet
import calendar

from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_state_printed import ensure_state_printed
import logging
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.pk_state_via_database import PkSqlite3DB
from PIL import Image, ImageFilter
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from datetime import datetime
from datetime import date
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from sources.functions.get_nx import get_nx
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_f import is_f
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
import logging

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def remove_issue_code():
    logging.debug(f'''issu_code is removed {'%%%FOO%%%' if LTA else ''}''')
