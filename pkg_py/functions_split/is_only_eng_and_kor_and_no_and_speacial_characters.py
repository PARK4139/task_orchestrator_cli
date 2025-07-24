import urllib
import tqdm
import timeit
import socket
import shlex
import pyglet
import mutagen
import browser_cookie3
import asyncio
from selenium.webdriver.common.keys import Keys
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.system_object.state_via_database import PkSqlite3DB
from gtts import gTTS
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style


def is_only_eng_and_kor_and_no_and_speacial_characters(text):
    import re
    pattern = "^[ㄱ-ㅎ가-힣0-9a-zA-Z~!@#$%^&*()_+|<>?:{}]+$"
    if re.search(pattern, text):
        return 1
    else:
        return 0
