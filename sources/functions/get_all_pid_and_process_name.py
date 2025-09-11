import random
import colorama
from seleniumbase import Driver

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from cryptography.hazmat.backends import default_backend
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES


def get_all_pid_and_process_name():
    import inspect
      # pywin32
    
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    """모든 프로세스명 돌려주는 함수"""
    process_info = ""

    def enum_windows_callback(hwnd, _):
        import psutil
        # todo : ref : func_n 출력 하지 말자
        # func_n=inspect.currentframe().f_code.co_name
        nonlocal process_info
        if win32gui.IsWindowVisible(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                process = psutil.Process(pid)
                process_name = process.name()
                process_info += f"창 handle={hwnd}, pid: {pid}, process_name: {process_name}\n"
            except psutil.NoSuchProcess:
                pass

    win32gui.EnumWindows(enum_windows_callback, None)
    return process_info
