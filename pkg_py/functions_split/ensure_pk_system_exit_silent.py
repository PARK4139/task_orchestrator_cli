def ensure_pk_system_exit_silent(os=None):
    import sys
    import ipdb
    try:
        sys.stdout.flush()
        sys.stderr.flush()
        if os is None:
            ipdb.set_trace()  # pk_option
        else:
            ipdb.post_mortem(sys.exc_info()[2])  # pk_option
    except Exception:
        pass  # JUST IN CASE
    try:
        os._exit(0)  # Silent and immediate exit (no cleanup)
    except Exception:
        sys.exit(0)  # Fallback: graceful exit
