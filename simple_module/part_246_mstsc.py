import webbrowser
import undetected_chromedriver as uc
import toml
import pyglet
import psutil
import platform
import keyboard
import chardet
from selenium.webdriver.common.action_chains import ActionChains
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os

from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from pkg_py.simple_module.part_005_get_nx import get_nx


def mstsc(ip=None, port=3389):
    import inspect
    # 내부망에서 유동ip일때 ip대신 hostname 추천
    func_n = inspect.currentframe().f_code.co_name
    # cmd=f'mstsc /v:{ip}:{port} /admin /w:640 /h:350 /multimon /NoConsentPrompt'
    # cmd=f'mstsc /admin /w:960 /h:540 /v:{ip}:{port} /multimon /NoConsentPrompt'
    # cmd=f'mstsc /admin /w:960 /h:540 /v:{ip}:{port} /multimon /NoConsentPrompt'
    # cmd=f'mstsc /admin /w:960 /h:1080 /v:{ip}:{port} /multimon /NoConsentPrompt'
    cmd = f'mstsc /v:{ip}:{port} /admin /w:1024 /h:768 /multimon '
    cmd_to_os(cmd, mode='a')
