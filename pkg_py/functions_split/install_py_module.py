
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
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.directories  import D_PROJECT
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.local_test_activate import LTA
from os.path import dirname
from cryptography.hazmat.primitives import padding
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def install_py_module(module_name):
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
