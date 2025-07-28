if __name__ == "__main__":
    try:
        import os
        import sys
        import subprocess
        import traceback
        from pathlib import Path

        from colorama import init as pk_colorama_init

        # from pkg_py.system_object.500_live_logic import copy, ensure_vpc_recovery_mode_entered, print_window_opened_list
        # , STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, PK_WSL_DISTRO_N
        # , print_red

        ensure_colorama_initialized_once()

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
        ensure_copied(str_working=script_cmd)
        ensure_printed(UNDERLINE)
        ensure_printed(f"{STAMP_TRY_GUIDE} {script_cmd}")
        ensure_printed(UNDERLINE)
