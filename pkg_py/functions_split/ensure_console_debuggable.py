def ensure_console_debuggable():
    from pkg_py.functions_split.pk_sleep import pk_sleep
    from pkg_py.functions_split.print_red import print_red
    print_red(f"[ PK DEBUGER WORKED ]")
    pk_sleep(hours=1, mode_countdown=0)
