import traceback
import tqdm
import sys
import shlex
import pythoncom
import math
import inspect

from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

from sources.functions.ensure_pressed import ensure_pressed

from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from pathlib import Path
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from bs4 import BeautifulSoup
from base64 import b64encode
from sources.functions.get_pnx_windows_style import get_pnx_windows_style


def edit_browser_url_like_human():
    import random
    ensure_pressed("ctrl", "l"
    5)
    ensure_pressed("right"
    5)
    write("/")
    ensure_slept(milliseconds=random.randint(a=12, b=23))
