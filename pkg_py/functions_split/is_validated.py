import secrets
import pythoncom
import importlib

from pkg_py.system_object.state_via_context import SpeedControlContext
from functools import lru_cache
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.get_d_working import get_d_working


def is_validated(target: any):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    if target is None:
        return 0
    if target == "":
        return 0
    if is_pattern_in_prompt(prompt=target, pattern=r'[^a-zA-Z0-9가-힣\s]',
                            with_case_ignored=False):  # 특수문자 패턴 정의( 알파벳, 숫자, 한글, 공백을 제외한 모든 문자)
        return 0
    else:
        return 1
