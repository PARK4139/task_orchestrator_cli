


def paste_and_enter():
    from pkg_py.functions_split.press import press
    from pkg_py.functions_split.ensure_slept import ensure_slept
    pk_press("ctrl+v")
    ensure_slept(200)
    pk_press("enter")
    # ensure_slept(500)


