





from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_writen_fast(string: str):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    ensure_slept(milliseconds=500)
    copy_and_paste_with_keeping_clipboard(string)
    ensure_printed(rf"{string}", print_color='blue')
