

import webbrowser
import toml
import subprocess
import sqlite3
import socket
import random

import pyautogui
import os
import numpy as np
import keyboard
import ipdb
import easyocr
import colorama
import calendar
import asyncio
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession

from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern

from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f

from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_map_texts import PkTexts

from PIL import Image, ImageFilter
from os.path import dirname
from os import path
from moviepy import VideoFileClip
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from base64 import b64encode
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES

from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
import logging


def get_random_address():
    pass
