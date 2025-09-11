


def paste_and_enter_like_human():
    from sources.functions.ensure_pressed import ensure_pressed
    from sources.functions.ensure_slept import ensure_slept
    ensure_pressed("ctrl+v")
    ensure_slept(200)
    ensure_pressed("enter")
    # ensure_slept(500)


