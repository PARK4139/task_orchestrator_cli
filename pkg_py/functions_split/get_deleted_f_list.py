import shutil
import pywintypes

import nest_asyncio
from tkinter import UNDERLINE
from PySide6.QtWidgets import QApplication
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.print_state import print_state

from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.system_object.directories import D_PK_WORKING

from fastapi import HTTPException
from datetime import timedelta
from datetime import datetime
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed


def get_deleted_f_list(previous_state, current_state):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    return DataStructureUtil.get_elements_that_list1_only_have(list1=previous_state, list2=current_state)
