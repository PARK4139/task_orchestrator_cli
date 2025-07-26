





from typing import TypeVar

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed

# , pk_measure_memory
# from pkg_py.system_object.time_and_lanauge_util import sleep

T = TypeVar('T')


def todo(id):
    ensure_printed(f'''여기 할 차례입니다. at {id}. {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    raise
