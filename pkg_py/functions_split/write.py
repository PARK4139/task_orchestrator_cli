



from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.copy_and_paste_with_keeping_clipboard import copy_and_paste_with_keeping_clipboard


def write(string: str, milliseconds=500):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    ensure_slept(milliseconds=milliseconds)
    copy_and_paste_with_keeping_clipboard(string)
    ensure_printed(rf"{string}", print_color='blue')
