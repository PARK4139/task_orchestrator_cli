

# import win32process
# import pywin32


from pkg_py.functions_split.pk_print import pk_print


def write_fast(string: str):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    pk_sleep(milliseconds=500)
    copy_and_paste_with_keeping_clipboard(string)
    pk_print(rf"{string}", print_color='blue')
