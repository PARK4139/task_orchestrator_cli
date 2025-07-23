

# import win32gui
# import pywin32
# import pywin32

from typing import TypeVar

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print

# , pk_measure_memory
# from pkg_py.pk_system_object.time_and_lanauge_util import pk_sleep

T = TypeVar('T')


def todo(id):
    pk_print(f'''여기 할 차례입니다. at {id}. {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    raise
