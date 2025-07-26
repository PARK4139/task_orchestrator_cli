def press_ctrl_alt_l_nth():
    n = 3
    for _ in range(n):
        ensure_slept(100)
        ensure_pressed("ctrl+alt+shift+l")
        ensure_slept(100)
        ensure_pressed("enter")
        ensure_slept(100)
    ensure_slept(100)


