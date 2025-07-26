import urllib.parse
import toml
import sys

import psutil
import keyboard
import datetime
import colorama
from urllib.parse import urlparse
from tkinter import UNDERLINE
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_database import PkSqlite3DB
from mutagen.mp3 import MP3
from functools import lru_cache
from fastapi import HTTPException
from datetime import date
from colorama import init as pk_colorama_init
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.ensure_printed import ensure_printed


def print_and_write_schedule_template_cyclic_to_f_memo_todo_txt(
        stamp_custom, todo_task_name_str, start_date, end_date, f_txt,
        period="daily", specific_day=None, specific_weekday=None, specific_week=None, specific_month=None
