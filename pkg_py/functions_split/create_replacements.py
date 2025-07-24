import win32con
import tarfile
import sys
import socket
import pandas as pd
import keyboard
import functools
import colorama
from urllib.parse import urlparse
from urllib.parse import quote
from seleniumbase import Driver
from pynput import mouse
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.state_via_context import SpeedControlContext
from pathlib import Path
from os import path
from mutagen.mp3 import MP3
from functools import partial as functools_partial
from bs4 import ResultSet
from pkg_py.functions_split.pk_print import pk_print


def create_replacements(extracted_words, size):
    unique_words = set(extracted_words)
    replacements = {f'{word}': f'{word:{size}s}' for word in unique_words}
    return replacements
