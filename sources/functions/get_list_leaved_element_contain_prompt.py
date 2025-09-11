import yt_dlp
import winreg
import webbrowser
import toml
import string
import speech_recognition as sr

import mysql.connector
import math
import ipdb
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote, urlparse
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from prompt_toolkit.styles import Style
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.pk_etc import PkFilter
from sources.objects.pk_map_texts import PkTexts

from sources.objects.pk_local_test_activate import LTA
from PIL import Image
from os import path
from moviepy import VideoFileClip
from datetime import datetime, time
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from base64 import b64encode
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.does_pnx_exist import is_pnx_existing


def get_list_leaved_element_contain_prompt(working_list, prompt):
    return [f for f in working_list if prompt in f]
