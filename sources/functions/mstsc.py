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
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working

from sources.functions.ensure_command_executed import ensure_command_executed

from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from sources.functions.get_nx import get_nx


def mstsc(ip=None, port=3389):
    import inspect
    # 내부망에서 유동ip일때 ip대신 hostname 추천
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    # cmd=f'mstsc /v:{ip}:{port} /admin /w:640 /h:350 /multimon /NoConsentPrompt'
    # cmd=f'mstsc /admin /w:960 /h:540 /v:{ip}:{port} /multimon /NoConsentPrompt'
    # cmd=f'mstsc /admin /w:960 /h:540 /v:{ip}:{port} /multimon /NoConsentPrompt'
    # cmd=f'mstsc /admin /w:960 /h:1080 /v:{ip}:{port} /multimon /NoConsentPrompt'
    cmd = f'mstsc /v:{ip}:{port} /admin /w:1024 /h:768 /multimon '
    ensure_command_executed(cmd, mode='a')
