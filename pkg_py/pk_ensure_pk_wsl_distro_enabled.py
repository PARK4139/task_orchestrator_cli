if __name__ == "__main__":

    import traceback
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.functions_split.ensure_pk_wsl_distro_enabled import ensure_pk_wsl_distro_enabled
    from pkg_py.system_object.directories  import D_PROJECT
    # pk_#

    try:
        ensure_colorama_initialized_once()

        if not ensure_pk_wsl_distro_enabled():
            raise RuntimeError("WSL 배포판 설치/이름 변경에 실패했습니다.")
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
