import traceback
import pyaudio
import paramiko
import os.path
import hashlib
import easyocr
import clipboard
from selenium.webdriver.common.keys import Keys
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.print_red import print_red
from PIL import Image
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from functools import lru_cache
from datetime import datetime
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def get_tuple_from_set(working_set):
    return tuple(working_set)
