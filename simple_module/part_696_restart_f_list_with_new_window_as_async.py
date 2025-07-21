import win32con
import tomllib
import socket
import requests
from urllib.parse import urlparse
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from collections import defaultdict, Counter
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA


def restart_f_list_with_new_window_as_async(f_list):
    import asyncio
    for f in f_list:
        asyncio.run(pk_kill_process_as_async(f=f))
    for f in f_list:
        asyncio.run(pk_run_process_as_async(f=f))
