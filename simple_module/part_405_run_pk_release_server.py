# import pywin32
import pyautogui
import platform
import functools
from selenium.webdriver.support.ui import WebDriverWait
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT

from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.simple_module.part_014_pk_print import pk_print


def run_pk_release_server(port):
    import inspect

    # explorer "http://localhost:9090"
    # curl -O http://49:9090/1.zip && exit
    func_n = inspect.currentframe().f_code.co_name

    py_pnx = rf'{D_PROJECT}\pk_system_{func_n}.py'
    if not does_pnx_exist(pnx=py_pnx):
        return

    if is_window_opened(window_title_seg=py_pnx):
        # kill_window_duplicated_list_in_loop()
        ensure_window_to_front(window_title_seg=py_pnx)
        return

    server_ip = "localhost"
    pk_print(f'''server_ip={server_ip}''')
    pk_print(f'''server_port={port}''')

    # bat_pnx=rf'{USERPROFILE}\Downloads\pk_system\pk_system_http_server_run.cmd'
    # cmd=rf'start cmd.exe /k "{bat_pnx}"'

    cmd = rf'start cmd.exe /k python "{py_pnx}"'
    cmd_to_os(cmd=cmd, mode="a")
    # pk_print(f'''{cmd} [Negative]"''')

    url = rf'http://{server_ip}:{port}'
    cmd = rf" explorer {url}/"
    cmd_to_os(cmd=cmd, mode="a")
    kill_chrome_tab_duplicated()
    move_chrome_tab_by_url(url=url)

    cmd = rf' netstat -ano | find "{port}" '
    cmd_to_os(cmd=cmd, mode="a")
