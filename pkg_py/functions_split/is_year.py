import zlib

import win32con
import urllib.parse
import tomllib
import time
import threading
import tarfile
import speech_recognition as sr
import shlex
import requests
import random

import pyglet
import pygetwindow
import pyaudio
import psutil
import pickle
import pandas as pd
import mysql.connector
import inspect
import easyocr
import cv2
import clipboard
import calendar
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pytube import Playlist
from pynput import mouse
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
# pk_#
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.local_test_activate import LTA
from PIL import Image
from os import path
from mutagen.mp3 import MP3
from functools import partial as functools_partial
from functools import partial
from fastapi import HTTPException
from datetime import datetime, time
from cryptography.hazmat.primitives import padding
from bs4 import ResultSet

from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.get_d_working import get_d_working


def is_year(yyyy):
    from datetime import datetime
    return datetime.today().year == int(yyyy)
