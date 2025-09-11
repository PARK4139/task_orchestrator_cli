import zipfile

import webbrowser
import undetected_chromedriver as uc
import tomllib
import time
import tarfile
import sys
import subprocess, time
import speech_recognition as sr
import socket, time
import re


import pyglet
import platform
import pandas as pd
import mysql.connector
import math
import keyboard
import ipdb
import importlib
import chardet
import calendar

from telethon import TelegramClient, events
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
import logging
from sources.functions.ensure_console_cleared import ensure_console_cleared

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI


from pathlib import Path
from gtts import gTTS
from functools import partial as functools_partial
from dirsync import sync
from datetime import date
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from sources.functions.get_nx import get_nx


from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.objects.pk_local_test_activate import LTA
from sources.functions.does_pnx_exist import is_pnx_existing

import logging


def get_element_random(working_list):
    import random
    return random.choice(working_list)
