import undetected_chromedriver as uc
import tqdm
import toml
import threading
import pyaudio
import mutagen
from selenium.webdriver.chrome.options import Options
from prompt_toolkit import PromptSession

from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.encodings import Encoding
from sources.objects.pk_local_test_activate import LTA
from datetime import timedelta
from bs4 import BeautifulSoup
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.get_pnxs import get_pnxs


def get_random_id(length_limit: int):
    import random
    import string

    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length_limit))
