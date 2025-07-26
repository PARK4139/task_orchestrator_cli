def ensure_losslesscut_reran(F_CACHE):
    from pkg_py.functions_split.run_losslesscut import run_losslesscut
    from pkg_py.functions_split.kill_losslesscut import kill_losslesscut
    from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
    kill_losslesscut()
    while 1:
        if not is_losslesscut_running(F_CACHE):
            run_losslesscut()
            break
