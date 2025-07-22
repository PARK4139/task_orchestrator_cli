



from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.copy_and_paste_with_keeping_clipboard import copy_and_paste_with_keeping_clipboard


def write(string: str, milliseconds=500):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    pk_sleep(milliseconds=milliseconds)
    copy_and_paste_with_keeping_clipboard(string)
    pk_print(rf"{string}", print_color='blue')
