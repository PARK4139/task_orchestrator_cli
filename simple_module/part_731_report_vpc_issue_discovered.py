import random
import pygetwindow
import chardet
from pytube import Playlist
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from passlib.context import CryptContext
from colorama import init as pk_colorama_init
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.pk_system_layer_100_os import is_os_windows

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def report_vpc_issue_discovered():
    pk_print(f'''vpc issue is discovered {'%%%FOO%%%' if LTA else ''}''', print_color='red')
