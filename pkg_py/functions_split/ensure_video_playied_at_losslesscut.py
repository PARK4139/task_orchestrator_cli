def ensure_video_playied_at_losslesscut():
    from pkg_py.functions_split.ensure_pressed import ensure_pressed
    from pkg_py.functions_split.ensure_slept import ensure_slept
    ensure_pressed("esc")
    ensure_slept(milliseconds=300)
    ensure_pressed("space")
