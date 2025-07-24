#!/usr/bin/env python   # shebang
# -*- coding: utf-8 -*- # encoding declaration
__author__ = 'pk == junghoon.park'

import sys
import traceback

from colorama import init as pk_colorama_init

# from pkg_py.system_object.500_live_logic import ensure_pk_wsl_distro_installed
#, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
#, print_red

pk_colorama_init_once()

if __name__ == "__main__":
    try:
        if not ensure_pk_wsl_distro_installed():
            raise RuntimeError("WSL 배포판 설치/이름 변경에 실패했습니다.")
    except Exception as ex:
        print_red(PK_UNDERLINE)
        for line in traceback.format_exception_only(type(ex), ex):
            print_red(f"{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {line.strip()}")
        print_red(PK_UNDERLINE)
        sys.exit(1)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
