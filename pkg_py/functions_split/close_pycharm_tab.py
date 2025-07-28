def close_pycharm_tab():
    from pkg_py.functions_split.ensure_pressed import ensure_pressed
    from pkg_py.functions_split.ensure_slept import ensure_slept
    ensure_pressed("ctrl", "f4")
    ensure_slept(100)
