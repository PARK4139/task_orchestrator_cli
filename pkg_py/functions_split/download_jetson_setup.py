import secrets
import numpy as np
import easyocr
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.directories import D_PK_WORKING
from cryptography.hazmat.backends import default_backend
from pkg_py.functions_split.get_nx import get_nx


def download_jetson_setup():
    todo('%%%FOO%%%')
