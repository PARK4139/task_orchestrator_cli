import winreg
import webbrowser
import pyglet
import pygetwindow
import psutil
import json
from selenium.common.exceptions import WebDriverException
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from colorama import init as pk_colorama_init
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist


def is_only_no(text):
    import re
    pattern = "^[0-9]+$"
    if re.search(pattern, text):
        return 1
    else:
        return 0
