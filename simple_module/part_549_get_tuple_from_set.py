import traceback
import pyaudio
import paramiko
import os.path
import hashlib
import easyocr
import clipboard
from selenium.webdriver.common.keys import Keys
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_800_print_util import print_red
from PIL import Image
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from functools import lru_cache
from datetime import datetime
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist


def get_tuple_from_set(working_set):
    return tuple(working_set)
