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
from sources.functions.get_historical_list import get_historical_list
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER

from sources.objects.pk_state_via_database import PkSqlite3DB
from mutagen.mp3 import MP3
from functools import lru_cache
from fastapi import HTTPException
from datetime import date
from colorama import init as pk_colorama_init
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_list_calculated import get_list_calculated
import logging


def print_and_write_schedule_template_cyclic_to_f_memo_todo_txt(
        stamp_custom, todo_task_name_str, start_date, end_date, f_txt,
        period="daily", specific_day=None, specific_weekday=None, specific_week=None, specific_month=None
