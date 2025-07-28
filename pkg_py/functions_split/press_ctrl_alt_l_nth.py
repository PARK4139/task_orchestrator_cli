def press_ctrl_alt_l_nth():
    from pkg_py.functions_split.ensure_pressed import ensure_pressed
    from pkg_py.functions_split.ensure_slept import ensure_slept

    # n = 3 # pk_option
    n = 2 # pk_option
    for _ in range(n):
        ensure_slept(100)
        ensure_pressed("ctrl+alt+shift+l")
        ensure_slept(100)
        ensure_pressed("enter")
        ensure_slept(100)
    ensure_slept(100)
