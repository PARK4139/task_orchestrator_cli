def get_text_dragged():
    from pkg_py.functions_split.ensure_pasted import ensure_pasted
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.functions_split.ensure_pressed import ensure_pressed

    import clipboard
    clipboard_current_contents = ensure_pasted()
    while 1:
        ensure_pressed("ctrl", "c")
        ensure_slept(milliseconds=15)
        text_dragged = ensure_pasted()
        if clipboard_current_contents != text_dragged:
            break
    clipboard.copy(clipboard_current_contents)
    return text_dragged


def get_text_dragged_alternative():
    from pkg_py.functions_split.ensure_pasted import ensure_pasted
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.ensure_printed import ensure_printed

    from pkg_py.functions_split.ensure_pressed import ensure_pressed

    import inspect
    import clipboard
    func_n = inspect.currentframe().f_code.co_name
    clipboard_current_contents = ensure_pasted()
    ensure_pressed("ctrl", "c")
    text_dragged = ensure_pasted()
    ensure_printed(str_working=rf'''text_dragged="{text_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
    clipboard.copy(clipboard_current_contents)

    return text_dragged
