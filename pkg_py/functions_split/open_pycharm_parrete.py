def open_pycharm_parrete():
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.functions_split.ensure_pressed import ensure_pressed

    ensure_pressed("shift")
    ensure_slept(100)
    ensure_pressed("shift")
    ensure_slept(500)
