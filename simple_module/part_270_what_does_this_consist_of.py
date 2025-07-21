import toml
import time
import subprocess
import string
import pyglet
import paramiko
import mutagen
import math
import asyncio
from selenium.webdriver.common.action_chains import ActionChains
from PySide6.QtWidgets import QApplication
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def what_does_this_consist_of(text: str):
    result = []
    if is_containing_kor(text=text):
        result.append("kor")
    if is_containing_eng(text=text):
        result.append("eng")
    if is_containing_number(text=text):
        result.append("number")
    if is_containing_special_characters_with_thread(text=text):
        result.append("special_characters")
    if is_containing_jpn(text=text):
        result.append("jpn")
    # print_magenta(rf'text : {text}   result : {result}')
    return result
