import undetected_chromedriver as uc
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.pk_system_layer_100_os import is_os_windows
from pathlib import Path
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor


def is_void_function(func):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    """
        함수가 void 함수인지 아닌지 판단하는 함수입니다.

        Args:
          function: 함수

        Returns:
          함수가 void 함수이면 True, 아니면 False
    """
    function_code = func.__code__
    return function_code.co_argcount == 0 and function_code.co_flags & 0x20 == 0
