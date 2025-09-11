def open_pycharm_parrete_like_human():
    from sources.functions.ensure_slept import ensure_slept
    from sources.functions.ensure_pressed import ensure_pressed

    ensure_pressed("shift")
    ensure_slept(100)
    ensure_pressed("shift")
    ensure_slept(500)
