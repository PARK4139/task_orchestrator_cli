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
from sources.functions.get_historical_list import get_historical_list


from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted

from sources.functions.set_pk_context_state import set_pk_context_state

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.pk_local_test_activate import LTA
from PIL import Image
from os import path
from mutagen.mp3 import MP3
from functools import partial as functools_partial
from functools import partial
from fastapi import HTTPException
from datetime import datetime, time
from cryptography.hazmat.primitives import padding
from bs4 import ResultSet

from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.get_pnxs import get_pnxs
from sources.functions.is_d import is_d
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def is_year(yyyy):
    from datetime import datetime
    return datetime.today().year == int(yyyy)
