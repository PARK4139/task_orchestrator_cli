import shutil
import pywintypes
# import pywin32
import nest_asyncio
from tkinter import UNDERLINE
from PySide6.QtWidgets import QApplication
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.pk_system_layer_directories import D_WORKING

from fastapi import HTTPException
from datetime import timedelta
from datetime import datetime
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_014_pk_print import pk_print


def get_deleted_f_list(previous_state, current_state):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    return DataStructureUtil.get_elements_that_list1_only_have(list1=previous_state, list2=current_state)
