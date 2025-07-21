import zlib
import toml
import string
import pyautogui
import keyboard
from tkinter import UNDERLINE
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared

from passlib.context import CryptContext
from functools import partial as functools_partial
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.pk_system_layer_100_Local_test_activate import LTA

from pkg_py.pk_system_layer_100_Local_test_activate import LTA


def shutdown_this_computer():
    cmd_to_os(rf'%windir%\System32\Shutdown.exe -s ')
