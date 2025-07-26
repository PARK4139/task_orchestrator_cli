import winreg
import webbrowser
import pyglet
import pygetwindow
import psutil
import json
from selenium.common.exceptions import WebDriverException
from prompt_toolkit import PromptSession
from pkg_py.functions_split.press import press
from pkg_py.functions_split.print_state import print_state
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from colorama import init as pk_colorama_init
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def is_only_no(text):
    import re
    pattern = "^[0-9]+$"
    if re.search(pattern, text):
        return 1
    else:
        return 0
