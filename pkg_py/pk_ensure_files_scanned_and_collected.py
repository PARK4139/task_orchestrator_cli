

if __name__ == "__main__":
    import sys
    import traceback

    from colorama import init as pk_colorama_init

    # from pkg_py.system_object.500_live_logic import copy, pk_ensure_files_scaned_and_collected
    #, '[ TRY GUIDE ]', D_PROJECT, '[ UNIT TEST EXCEPTION DISCOVERED ]'
    #, print_red

    try:
        ensure_colorama_initialized_once()

        pk_ensure_files_scaned_and_collected()
    except Exception as ex:
        print_red(PK_UNDERLINE)
        for line in traceback.format_exception_only(type(ex), ex):
            print_red(f'{'[ UNIT TEST EXCEPTION DISCOVERED ]'} {line.strip()}')
        print_red(PK_UNDERLINE)
        sys.exit(1)
    finally:
        script_cmd = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        
        ensure_printed(PK_UNDERLINE)
        ensure_printed(f"{'[ TRY GUIDE ]'} {script_cmd}")
        ensure_printed(PK_UNDERLINE)
