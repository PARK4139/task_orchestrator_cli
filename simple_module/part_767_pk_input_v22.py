import zipfile
# import win32process
import webbrowser
import traceback
import shlex
import platform
import numpy as np
import datetime
import colorama
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit.styles import Style
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from cryptography.hazmat.backends import default_backend
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style

from pkg_py.simple_module.part_014_pk_print import pk_print


def pk_input_v22(
        working_str: str,
        limit_seconds: int = 30,
        return_default: str | None = None,
        *,
        get_input_validated=None,  # bool 반환 함수
        verbose_log: bool = True,
        masked: bool = False,
        auto_repeat: bool = False,
        fuzzy_accept: list[tuple[str, ...]] | None = None,
