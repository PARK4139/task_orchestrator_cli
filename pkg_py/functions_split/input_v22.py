
*,
auto_repeat: bool = False,
def pk_input_v22(
from cryptography.hazmat.backends import default_backend
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.print import pk_print
from prompt_toolkit.styles import Style
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
fuzzy_accept: list[tuple[str, ...]] | None = None,
get_input_validated=None,  # bool 반환 함수
import colorama
import datetime
import numpy as np
import platform
import shlex
import traceback
import webbrowser
import zipfile
limit_seconds: int = 30,
masked: bool = False,
return_default: str | None = None,
str_working: str,
verbose_log: bool = True,
