
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
from sources.functions.is_window_title_front import is_window_title_front
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from passlib.context import CryptContext
from gtts import gTTS
from functools import partial
from datetime import date
from bs4 import BeautifulSoup
from pathlib import Path
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES


def get_windows_opened_with_hwnd_via_pygetwindow():
    import pygetwindow
    windows = pygetwindow.getAllTitles()
    return windows
