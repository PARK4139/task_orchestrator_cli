import zlib
import toml
import string
import pyautogui
import keyboard
from tkinter import UNDERLINE
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared

from passlib.context import CryptContext
from functools import partial as functools_partial
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.system_object.local_test_activate import LTA


def shutdown_this_computer():
    cmd_to_os(rf'%windir%\System32\Shutdown.exe -s ')
