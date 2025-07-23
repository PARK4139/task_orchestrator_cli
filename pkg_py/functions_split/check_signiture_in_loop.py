import yt_dlp
import uuid
import tarfile
import nest_asyncio
import json
import chardet
from zipfile import BadZipFile
from pytube import Playlist
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.pk_print_state import pk_print_state

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.write_list_to_f import write_list_to_f

from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pathlib import Path
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def check_signiture_in_loop(time_limit, working_list, signiture, signiture_found_ment):
    import time

    lines = working_list
    time_s = time.time()
    while 1:
        for line in lines:
            if signiture in line:
                if LTA:
                    pk_print(working_str=rf'''{signiture_found_ment}  {'%%%FOO%%%' if LTA else ''}''',
                             print_color="green")
                return 1
        if time.time() - time_s > time_limit:
            return 0
        pk_sleep(seconds=0.5)
