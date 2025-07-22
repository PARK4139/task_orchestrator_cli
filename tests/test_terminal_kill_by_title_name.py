import subprocess
import time

import win32con
import win32gui

from pkg_py.workspace.pk_workspace import pk_kill_process_v7


def open_dummpy_cmd_exe_with_title(window_title):
    subprocess.Popen(
        ['cmd.exe', '/k', f'title {window_title}'],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )


if __name__ == "__main__":
    test_title = "pk_test2.py"
    for _ in range(10):
        open_dummpy_cmd_exe_with_title(test_title)

    # 창 제목 반영 대기
    time.sleep(1)

    # 창 모두 닫기
    pk_kill_process_v7(test_title)
