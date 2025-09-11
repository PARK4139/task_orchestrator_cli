import zipfile
import win32con
import subprocess, time
import string
import requests

import pythoncom
import pygetwindow
import psutil
import mutagen
import datetime
from zipfile import BadZipFile
from tkinter import UNDERLINE
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style


from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.encodings import Encoding
from sources.objects.pk_state_via_database import PkSqlite3DB
from PIL import Image
from os import path
from functools import lru_cache
from base64 import b64decode
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.is_f import is_f
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging


def get_list_contained_with_stamp_from_f(f, STAMP):
    list_filtered = get_list_from_f(f=f)
    logging.debug(f'''STAMP={STAMP}  {'%%%FOO%%%' if LTA else ''}''')
    list_filtered = get_list_contained_element(working_list=list_filtered, prefix=rf"{STAMP} ")
    logging.debug(f'''list_filtered={list_filtered}  {'%%%FOO%%%' if LTA else ''}''')
    list_filtered = get_list_deduplicated(working_list=list_filtered)
    logging.debug(f'''list_filtered={list_filtered}  {'%%%FOO%%%' if LTA else ''}''')
    list_filtered = get_list_removed_element_contain_prompt(working_list=list_filtered, prompt="#")
    logging.debug(f'''list_filtered={list_filtered}  {'%%%FOO%%%' if LTA else ''}''')
    list_filtered = get_list_replaced_element_from_str_to_str(working_list=list_filtered, from_str=STAMP, to_str="")
    logging.debug(f'''list_filtered={list_filtered}  {'%%%FOO%%%' if LTA else ''}''')
    list_filtered = get_list_striped_element(working_list=list_filtered)
    logging.debug(f'''list_filtered={list_filtered}  {'%%%FOO%%%' if LTA else ''}''')
    return list_filtered
