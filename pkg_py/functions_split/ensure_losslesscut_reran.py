def ensure_losslesscut_reran():
    from pkg_py.functions_split.ensure_losslesscut_ran import ensure_losslesscut_ran
    from pkg_py.functions_split.kill_losslesscut import kill_losslesscut
    from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
    kill_losslesscut()
    while 1:
        if not is_losslesscut_running():
            ensure_losslesscut_ran()
            break
