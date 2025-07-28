

if __name__ == "__main__":
    import sys
    import traceback

    from colorama import init as pk_colorama_init

    # from pkg_py.system_object.500_live_logic import copy, pk_ensure_f_list_scaned_and_collected
    #, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
    #, print_red

    try:
        ensure_colorama_initialized_once()

        pk_ensure_f_list_scaned_and_collected()
    except Exception as ex:
        print_red(PK_UNDERLINE)
        for line in traceback.format_exception_only(type(ex), ex):
            print_red(f'{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {line.strip()}')
        print_red(PK_UNDERLINE)
        sys.exit(1)
    finally:
        script_cmd = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        
        ensure_printed(UNDERLINE)
        ensure_printed(f"{STAMP_TRY_GUIDE} {script_cmd}")
        ensure_printed(UNDERLINE)
