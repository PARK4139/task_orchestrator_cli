import zipfile
import win32con
import subprocess, time
import string
import requests
# import pywin32
import pythoncom
import pygetwindow
import psutil
import mutagen
import datetime
from zipfile import BadZipFile
from tkinter import UNDERLINE
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from PIL import Image
from os import path
from functools import lru_cache
from base64 import b64decode
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def get_list_contained_with_stamp_from_f(f, STAMP):
    list_filtered = get_list_from_f(f=f)
    pk_print(f'''STAMP={STAMP}  {'%%%FOO%%%' if LTA else ''}''')
    list_filtered = get_list_contained_element(working_list=list_filtered, prefix=rf"{STAMP} ")
    pk_print(f'''list_filtered={list_filtered}  {'%%%FOO%%%' if LTA else ''}''')
    list_filtered = get_list_deduplicated(working_list=list_filtered)
    pk_print(f'''list_filtered={list_filtered}  {'%%%FOO%%%' if LTA else ''}''')
    list_filtered = get_list_removed_element_contain_prompt(working_list=list_filtered, prompt="#")
    pk_print(f'''list_filtered={list_filtered}  {'%%%FOO%%%' if LTA else ''}''')
    list_filtered = get_list_replaced_element_from_str_to_str(working_list=list_filtered, from_str=STAMP, to_str="")
    pk_print(f'''list_filtered={list_filtered}  {'%%%FOO%%%' if LTA else ''}''')
    list_filtered = get_list_striped_element(working_list=list_filtered)
    pk_print(f'''list_filtered={list_filtered}  {'%%%FOO%%%' if LTA else ''}''')
    return list_filtered
