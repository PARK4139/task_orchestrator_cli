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
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
# from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.performance_logic import ensure_seconds_measured, pk_measure_memory
from pkg_py.system_object.get_list_calculated import get_list_calculated
from PIL import Image, ImageFilter
from mutagen.mp3 import MP3
from datetime import timedelta
from dataclasses import dataclass
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def download_vpc_aifw_docker_image(vpc_data, config_remote_os):
    if vpc_data.vpc_type == 'no':
        todo('%%%FOO%%%')
