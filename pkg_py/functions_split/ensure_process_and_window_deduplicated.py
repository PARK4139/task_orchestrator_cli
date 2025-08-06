"""
WSL 환경에서 smart_person_ai 컨테이너 생성 확인 테스트
"""
import subprocess
import os
import sys
import platform
from typing import Dict
from pathlib import Path


def ensure_process_and_window_deduplicated():
    from pkg_py.functions_split.get_windows_opened import get_windows_opened
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_windows_closed import ensure_windows_closed
    from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
    from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
    from pkg_py.functions_split.ensure_func_info_loaded import ensure_func_info_loaded
    
    import threading

    flag_to_detect_enter = 0  # 루프제어용

    def listen_enter():
        global flag_to_detect_enter
        while 1:
            input()
            flag_to_detect_enter = 1

    def run_main_loop():
        global flag_to_detect_enter
        previous_windows_opened_list = get_windows_opened()
        len_before: int = 0
        
        while 1:
            # 윈도우 중복 제거
            current_windows_opened_list = get_windows_opened()
            len_current = len(current_windows_opened_list)
            
            if len_before != len_current:
                ensure_printed(f'''len_before={len_before}  {'%%%FOO%%%' if LTA else ''}''')
                ensure_printed(f'''len_current={len_current}  {'%%%FOO%%%' if LTA else ''}''')
                ensure_iterable_printed_as_vertical(item_iterable=current_windows_opened_list,
                                                  item_iterable_n="current_windows_opened_list")
                len_before = len_current
                
            if len(current_windows_opened_list) != len(previous_windows_opened_list):
                # 창 중복 제거를 위한 기본 창 제목들
                default_windows_to_close = ["Everything", "explorer.exe", "cmd.exe", "powershell.exe"]
                for window_title in default_windows_to_close:
                    ensure_windows_closed(window_title)
                    
                title = ensure_func_info_loaded(func_n="ensure_windows_closed")["title"]
                ensure_window_to_front(window_title_seg=title)
                previous_windows_opened_list = current_windows_opened_list

            ensure_slept(seconds=1)
            ensure_console_cleared()

    # start thread ( in background )
    thread = threading.Thread(target=listen_enter, daemon=True)
    thread.start()

    # run main loop
    run_main_loop()


if __name__ == "__main__":
    ensure_process_and_window_deduplicated()
