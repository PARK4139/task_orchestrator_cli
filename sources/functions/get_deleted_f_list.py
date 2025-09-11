import shutil
import pywintypes

import nest_asyncio
from tkinter import UNDERLINE
from PySide6.QtWidgets import QApplication


from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
import logging

from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING

from fastapi import HTTPException
from datetime import timedelta
from datetime import datetime
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
import logging


def get_deleted_f_list(previous_state, current_state):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    return DataStructureUtil.get_elements_that_list1_only_have(list1=previous_state, list2=current_state)
