import undetected_chromedriver as uc
import tqdm
import toml
import threading
import pyaudio
import mutagen
from selenium.webdriver.chrome.options import Options
from prompt_toolkit import PromptSession
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.local_test_activate import LTA
from datetime import timedelta
from bs4 import BeautifulSoup
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_list import get_pnx_list


def get_random_id(length_limit: int):
    import random
    import string

    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length_limit))
