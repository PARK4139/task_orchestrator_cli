import traceback

from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.ensure_pk_wsl_distro_installed import ensure_pk_wsl_distro_installed
from pkg_py.functions_split.colorama_init_once import colorama_init_once
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

colorama_init_once()

if __name__ == "__main__":
    try:
        if not ensure_pk_wsl_distro_installed():
            raise RuntimeError("WSL 배포판 설치/이름 변경에 실패했습니다.")
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
