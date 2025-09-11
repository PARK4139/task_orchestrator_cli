import random
import pygetwindow
import chardet
from pytube import Playlist
from sources.functions.get_d_working import get_d_working
from sources.functions.get_list_sorted import get_list_sorted
from passlib.context import CryptContext
from colorama import init as pk_colorama_init

from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed


from sources.objects.pk_local_test_activate import LTA
import logging


def report_target_issue_discovered():
    logging.debug(f'''vpc issue is discovered {'%%%FOO%%%' if LTA else ''}''')
