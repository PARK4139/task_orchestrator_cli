import win32con
import win32com.client
import webbrowser
import tarfile
import sys
import string
import sqlite3
import socket
import re
import random

import pyglet
import pygetwindow
import pyautogui
import paramiko
import importlib
import easyocr
import clipboard
import chardet

from urllib.parse import quote, urlparse
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession

from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_state_printed import ensure_state_printed
from sources.objects.pk_etc import PkFilter


from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from passlib.context import CryptContext
from moviepy import VideoFileClip
from gtts import gTTS
from dirsync import sync
from datetime import datetime
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from sources.functions.get_nx import get_nx

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.is_f import is_f
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
import logging

import logging


def run_target_aifw_docker_container (target_device_data, remote_device_target_config):
    if target_device_data.target_device_type == 'no':
        remote_device_target_config(cmd='sudo run_container -b', **remote_device_target_config)
