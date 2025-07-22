def press_ctrl_alt_l_nth():
    n = 3
    for _ in range(n):
        pk_sleep(100)
        pk_press("ctrl+alt+shift+l")
        pk_sleep(100)
        pk_press("enter")
        pk_sleep(100)
    pk_sleep(100)


