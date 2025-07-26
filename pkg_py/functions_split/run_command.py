def run_command(cmd: str, capture_output=False):
    import traceback

    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

    import subprocess
    try:
        if capture_output:
            result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
            return result.returncode, result.stdout + result.stderr
        else:
            result = subprocess.run(cmd, shell=True)
            return result.returncode, ""
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
