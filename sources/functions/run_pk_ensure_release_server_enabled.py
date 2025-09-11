
import pyautogui
import platform
import functools
from selenium.webdriver.support.ui import WebDriverWait
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI

from sources.functions.does_pnx_exist import is_pnx_existing

import logging


def run_pk_ensure_release_server_ran(port):
    import inspect

    # explorer "http://localhost:9090"
    # curl -O http://49:9090/1.zip && exit
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    py_pnx = rf'{D_TASK_ORCHESTRATOR_CLI}\task_orchestrator_cli_{func_n}.py'
    if not is_pnx_existing(pnx=py_pnx):
        return

    if is_window_opened(window_title_seg=py_pnx):
        # kill_window_duplicated_list_in_loop()
        ensure_window_to_front(py_pnx)
        return

    server_ip = "localhost"
    logging.debug(f'''server_ip={server_ip}''')
    logging.debug(f'''server_port={port}''')

    # bat_pnx=rf'{USERPROFILE}\Downloads\task_orchestrator_cli\task_orchestrator_cli_http_server_run.cmd'
    # cmd=rf'start cmd.exe /k "{bat_pnx}"'

    cmd = rf'start cmd.exe /k python "{py_pnx}"'
    ensure_command_executed(cmd=cmd, mode="a")
    # logging.debug(f'''{cmd} [Negative]"''')

    url = rf'http://{server_ip}:{port}'
    cmd = rf" explorer {url}/"
    ensure_command_executed(cmd=cmd, mode="a")
    kill_chrome_tab_duplicated()
    ensure_chrome_tab_moved_to_url(url=url)

    cmd = rf' netstat -ano | find "{port}" '
    ensure_command_executed(cmd=cmd, mode="a")
