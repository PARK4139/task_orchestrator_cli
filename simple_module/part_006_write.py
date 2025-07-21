

from pkg_py.simple_module.part_009_pk_sleep import pk_sleep

from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_203_copy_and_paste_with_keeping_clipboard import copy_and_paste_with_keeping_clipboard


def write(string: str, milliseconds=500):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    pk_sleep(milliseconds=milliseconds)
    copy_and_paste_with_keeping_clipboard(string)
    pk_print(rf"{string}", print_color='blue')
