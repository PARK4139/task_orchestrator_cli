import zipfile
import tqdm
import toml
import timeit
import mysql.connector
import importlib
import colorama
import calendar
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from prompt_toolkit import PromptSession
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.performance_logic import pk_measure_seconds, pk_measure_memory
from pkg_py.system_object.get_list_calculated import get_list_calculated
from PIL import Image, ImageFilter
from mutagen.mp3 import MP3
from datetime import timedelta
from dataclasses import dataclass
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def download_vpc_aifw_docker_image(vpc_data, config_remote_os):
    if vpc_data.vpc_type == 'no':
        todo('%%%FOO%%%')
