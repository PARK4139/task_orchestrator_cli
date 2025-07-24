import traceback
import tqdm
import sys
import shlex
import pythoncom
import math
import inspect
import browser_cookie3
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.pk_press import pk_press

from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pathlib import Path
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from bs4 import BeautifulSoup
from base64 import b64encode
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style


def edit_browser_url_like_person():
    import random
    pk_press("ctrl", "l"
    5)
    pk_press("right"
    5)
    write("/")
    pk_sleep(milliseconds=random.randint(a=12, b=23))
