def ensure_console_debuggable(ipdb):
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.functions_split.print_red import print_red

    ipdb.set_trace()  # pk_option # pk_fail
    # ensure_slept(hours=1, mode_countdown=0) # pk_option
