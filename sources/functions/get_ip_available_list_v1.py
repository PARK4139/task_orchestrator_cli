

import zlib
import winreg


import win32con
import webbrowser
import urllib.parse
import tomllib
import toml
import timeit
import threading
import tarfile
import subprocess
import string
import sqlite3
import speech_recognition as sr
import socket, time
import socket
import shutil
import shlex
import secrets
import requests
import re
import random, math
import random
import pywintypes

import pygetwindow
import pyaudio
import psutil
import platform
import pickle
import os.path
import os, inspect
import os
import nest_asyncio
import mysql.connector
import mutagen
import math
import keyboard
import importlib
import hashlib
import datetime
import cv2
import colorama
import colorama
import clipboard
import calendar

import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import urlparse
from urllib.parse import quote
from telethon import TelegramClient, events
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession

from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern


from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f

from sources.objects.pk_etc import PkFilter


from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING, D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING

from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext



from PIL import Image, ImageFont, ImageDraw, ImageFilter
from PIL import Image, ImageFilter
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from os import path
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from datetime import datetime, time
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from collections import Counter
from bs4 import ResultSet
from base64 import b64encode
from base64 import b64decode
from sources.functions.get_nx import get_nx

from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f

from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

import logging
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def get_ip_available_list_v1():
    ip_conncetion_test_result = get_ip_conncetion_ping_test_result_list()
    available_ip_list = [result for result in ip_conncetion_test_result if result[2] == 1]
    available_ip_list = sorted(available_ip_list)
    return available_ip_list
