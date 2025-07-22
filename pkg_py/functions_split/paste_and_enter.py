


def paste_and_enter():
    from pkg_py.functions_split.pk_press import pk_press
    from pkg_py.functions_split.pk_sleep import pk_sleep
    pk_press("ctrl+v")
    pk_sleep(200)
    pk_press("enter")
    # pk_sleep(500)


