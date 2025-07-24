def ensure_console_debuggable(ipdb):
    from pkg_py.functions_split.pk_sleep import pk_sleep
    from pkg_py.functions_split.print_red import print_red

    ipdb.set_trace()  # pk_option
    # pk_sleep(hours=1, mode_countdown=0) # pk_option
