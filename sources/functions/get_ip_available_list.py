

import zlib
import zipfile


import urllib
import tqdm
import tomllib
import tomllib
import toml
import timeit
import time
import subprocess, time
import sqlite3
import speech_recognition as sr
import shlex
import re
import random
import pyglet
import pygetwindow
import psutil
import platform
import paramiko
import pandas as pd
import os.path
import numpy as np
import mysql.connector
import keyboard
import json
import importlib
import easyocr
import datetime
import colorama
import colorama
import clipboard
import calendar

from urllib.parse import quote
from telegram import Bot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from queue import Queue, Empty
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession

from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.ensure_pressed import ensure_pressed
import logging
import logging
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.set_pk_context_state import set_pk_context_state

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING
from sources.objects.pk_state_via_context import SpeedControlContext

from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from functools import partial
from datetime import timedelta
from datetime import datetime
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64decode
from sources.functions.is_f import is_f
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA


def get_ip_available_list():
    return get_ip_available_list_v4()
