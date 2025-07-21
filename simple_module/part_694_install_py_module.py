# import win32gui
import win32con
import toml
import threading
import socket
import shutil
import shlex
import math
import clipboard
from seleniumbase import Driver
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from os.path import dirname
from cryptography.hazmat.primitives import padding
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist


def install_py_module(module_name):
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
