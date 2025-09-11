import yt_dlp
import uuid
import tarfile
import nest_asyncio
import json
import chardet
from zipfile import BadZipFile
from pytube import Playlist
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_window_to_front import ensure_window_to_front

import logging

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f

from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext
from pathlib import Path
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.ensure_slept import ensure_slept

from sources.objects.pk_local_test_activate import LTA
import logging


def check_signiture_in_loop(time_limit, working_list, signiture, signiture_found_ment):
    import time

    lines = working_list
    time_s = time.time()
    while 1:
        for line in lines:
            if signiture in line:
                if LTA:
                    logging.debug(rf'''{signiture_found_ment}  {'%%%FOO%%%' if LTA else ''}''')
                return 1
        if time.time() - time_s > time_limit:
            return 0
        ensure_slept(seconds=0.5)
