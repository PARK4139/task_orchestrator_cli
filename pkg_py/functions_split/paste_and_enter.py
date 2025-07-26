


def paste_and_enter():
    from pkg_py.functions_split.ensure_pressed import ensure_pressed
    from pkg_py.functions_split.ensure_slept import ensure_slept
    ensure_pressed("ctrl+v")
    ensure_slept(200)
    ensure_pressed("enter")
    # ensure_slept(500)


