def rerun_losslesscut(F_CACHE):
    from pkg_py.simple_module.part_473_run_losslesscut import run_losslesscut
    from pkg_py.simple_module.part_476_kill_losslesscut import kill_losslesscut
    from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
    kill_losslesscut()
    while 1:
        if not is_losslesscut_running(F_CACHE):
            run_losslesscut()
            break
