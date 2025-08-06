
import pyautogui
import platform
import functools
from selenium.webdriver.support.ui import WebDriverWait
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.directories  import D_PROJECT

from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.ensure_printed import ensure_printed


def run_pk_ensure_release_server_ran(port):
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
    ensure_printed(f'''server_ip={server_ip}''')
    ensure_printed(f'''server_port={port}''')

    # bat_pnx=rf'{USERPROFILE}\Downloads\pk_system\pk_system_http_server_run.cmd'
    # cmd=rf'start cmd.exe /k "{bat_pnx}"'

    cmd = rf'start cmd.exe /k python "{py_pnx}"'
    ensure_command_excuted_to_os(cmd=cmd, mode="a")
    # ensure_printed(f'''{cmd} [Negative]"''')

    url = rf'http://{server_ip}:{port}'
    cmd = rf" explorer {url}/"
    ensure_command_excuted_to_os(cmd=cmd, mode="a")
    kill_chrome_tab_duplicated()
    move_chrome_tab_by_url(url=url)

    cmd = rf' netstat -ano | find "{port}" '
    ensure_command_excuted_to_os(cmd=cmd, mode="a")
