import traceback
import sqlite3

import pickle
import keyboard
import inspect
from yt_dlp import YoutubeDL
from tkinter import UNDERLINE
from seleniumbase import Driver


from sources.objects.pk_state_via_context import SpeedControlContext
from passlib.context import CryptContext
from colorama import init as pk_colorama_init
from sources.functions.is_d import is_d

from sources.functions.get_pnx_windows_style import get_pnx_windows_style

import logging


def get_random_special_character(length_limit: int):
    import random
    import string

    result = ''
    for _ in range(length_limit):
        result += random.choice(string.printable)
    return
