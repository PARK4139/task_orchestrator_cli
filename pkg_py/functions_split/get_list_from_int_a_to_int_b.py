import sys
import clipboard
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_object.PkMessages2025 import PkMessages2025
from functools import partial
from fastapi import HTTPException

from pkg_py.functions_split.get_d_working import get_d_working


def get_list_from_int_a_to_int_b(int_a: int, int_b: int) -> list[int]:
    step = 1 if int_b >= int_a else -1
    return list(range(int_a, int_b + step, step))
