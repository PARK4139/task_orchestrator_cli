import traceback
import pyaudio
import paramiko
import os.path
import hashlib
import easyocr
import clipboard
from selenium.webdriver.common.keys import Keys
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.pk_system_object.etc import PkFilter
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.print_red import print_red
from PIL import Image
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from functools import lru_cache
from datetime import datetime
from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def get_tuple_from_set(working_set):
    return tuple(working_set)
