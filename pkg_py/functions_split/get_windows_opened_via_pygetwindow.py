
import webbrowser
import uuid
import sqlite3
import random
import pythoncom
import mysql.connector
import importlib
import colorama
import calendar
from zipfile import BadZipFile
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from prompt_toolkit import PromptSession
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.directories  import D_PROJECT
from passlib.context import CryptContext
from gtts import gTTS
from functools import partial
from datetime import date
from bs4 import BeautifulSoup
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.system_object.directories import D_PKG_PY


def get_windows_opened_via_pygetwindow():
    import pygetwindow
    windows = pygetwindow.getAllTitles()
    return windows
