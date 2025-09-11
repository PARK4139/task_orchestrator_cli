import undetected_chromedriver as uc


from pathlib import Path
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor


def is_void_function(func):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    """
        함수가 void 함수인지 아닌지 판단하는 함수입니다.

        Args:
          function: 함수

        Returns:
          함수가 void 함수이면 True, 아니면 False
    """
    function_code = func.__code__
    return function_code.co_argcount == 0 and function_code.co_flags & 0x20 == 0
