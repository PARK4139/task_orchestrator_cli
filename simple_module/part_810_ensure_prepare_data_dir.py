import urllib
import undetected_chromedriver as uc
import tomllib
import toml
import mutagen
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from pytube import Playlist
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f

from pkg_py.simple_module.part_014_pk_print import pk_print


def ensure_prepare_data_dir(container: str):
    import os

    data_dir = os.path.join(os.path.expanduser("~"), "Downloads", f"{container}_data")
    os.makedirs(data_dir, exist_ok=True)
    pk_print(f"Data directory ready: {data_dir}")
    return data_dir
