#!/usr/bin/env python   # shebang
# -*- coding: utf-8 -*- # encoding declaration
__author__ = 'pk == junghoon.park'


if __name__ == "__main__":
    try:
        import os
        import sys
        import subprocess
        import traceback
        from pathlib import Path

        from colorama import init as pk_colorama_init
        # from pkg_py.pk_system_object.500_live_logic import pk_copy, ensure_vpc_recovery_mode_entered, print_window_opened_list
        #, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, PK_WSL_DISTRO_N
        #, print_red

        pk_colorama_init_once()

        print_window_opened_list()

    except Exception as ex:
        print_red(PK_UNDERLINE)
        for line in traceback.format_exception_only(type(ex), ex):
            print_red(f'{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {line.strip()}')
        print_red(PK_UNDERLINE)
        sys.exit(1)

    finally:
        script_cmd = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        print(f"\n")
        pk_copy(working_str=script_cmd)
        pk_print(UNDERLINE)
        pk_print(f"{STAMP_TRY_GUIDE} {script_cmd}")
        pk_print(UNDERLINE)
