import sys
import socket
import pythoncom
import pygetwindow
import pyaudio
import importlib
from selenium.common.exceptions import WebDriverException
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.directories  import D_PROJECT
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.get_list_calculated import get_list_calculated
from functools import partial
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx


def get_target_gigabite(target_path):
    return get_target_bite(target_path.strip()) / 1024 ** 3
