def run_command(cmd: str, capture_output=False):
    import traceback

    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.system_object.directories  import D_PROJECT
    # pk_#

    import subprocess
    try:
        if capture_output:
            result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
            return result.returncode, result.stdout + result.stderr
        else:
            result = subprocess.run(cmd, shell=True)
            return result.returncode, ""
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
