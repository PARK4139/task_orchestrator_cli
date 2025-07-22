import uuid
import tarfile
import re
import pyglet
import json
import importlib
import datetime
import browser_cookie3
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_object.stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.state_via_context import SpeedControlContext

from os.path import dirname
from os import path
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style

from pkg_py.functions_split.get_pnx_list import get_pnx_list


def get_youtube_clip_id(url):
    youtube_clip_id = url.split("v=")[-1]
    return youtube_clip_id
