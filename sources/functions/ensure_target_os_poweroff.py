

import winreg


import win32con
import win32con
import undetected_chromedriver as uc
import traceback
import toml
import time
import socket
import secrets
import random
import pywintypes

import os
import numpy as np
import mysql.connector
import json
import importlib
import colorama
import clipboard
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote, urlparse
from urllib.parse import quote
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException

from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.get_d_working import get_d_working
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_state_via_database import PkSqlite3DB

from paramiko import SSHClient, AutoAddPolicy
from os import path
from functools import partial as functools_partial
from dataclasses import dataclass
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from bs4 import BeautifulSoup

from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.is_f import is_f
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.objects.pk_local_test_activate import LTA
import logging

from sources.functions.get_pnxs import get_pnxs


def ensure_target_os_poweroff():
    pass
