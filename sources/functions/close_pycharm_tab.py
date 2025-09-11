def close_pycharm_tab_like_human \
                ():
    from sources.functions.ensure_pressed import ensure_pressed
    from sources.functions.ensure_slept import ensure_slept
    ensure_pressed("ctrl", "f4")
    ensure_slept(100)
