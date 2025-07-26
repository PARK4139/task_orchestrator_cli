

if __name__ == "__main__":

    try:
        colorama_init_once()

        pk_delete_empty_d_list()
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
