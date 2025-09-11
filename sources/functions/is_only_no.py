import winreg
import webbrowser
import pyglet
import pygetwindow
import psutil
import json
from selenium.common.exceptions import WebDriverException
from prompt_toolkit import PromptSession
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from colorama import init as pk_colorama_init
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.does_pnx_exist import is_pnx_existing


def is_only_no(text):
    import re
    pattern = "^[0-9]+$"
    if re.search(pattern, text):
        return 1
    else:
        return 0
