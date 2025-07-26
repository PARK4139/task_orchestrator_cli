def press_ctrl_alt_l_nth():
    n = 3
    for _ in range(n):
        ensure_slept(100)
        pk_press("ctrl+alt+shift+l")
        ensure_slept(100)
        pk_press("enter")
        ensure_slept(100)
    ensure_slept(100)


