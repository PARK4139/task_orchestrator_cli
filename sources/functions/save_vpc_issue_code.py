import yt_dlp

import urllib.parse
import urllib
import tomllib
import timeit
import subprocess
import socket, time
import pyautogui
import os
import mutagen
import hashlib
import clipboard
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from telegram import Bot
from selenium.webdriver.common.by import By

import logging

from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.pk_etc import PkFilter
from PIL import Image, ImageFilter
from functools import partial as functools_partial
from datetime import timedelta
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from sources.functions.get_nx import get_nx
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided

from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.objects.pk_local_test_activate import LTA

from sources.objects.pk_local_test_activate import LTA
import logging


def save_target_issue_code(issue_code):
    logging.debug(f'''issu_code is saved {'%%%FOO%%%' if LTA else ''}''')
