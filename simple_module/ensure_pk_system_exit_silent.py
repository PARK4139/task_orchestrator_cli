

def ensure_pk_system_exit_silent():
    import sys
    import os
    try:
        sys.stdout.flush()
        sys.stderr.flush()
    except Exception:
        pass  # JUST IN CASE
    try:
        os._exit(0)  # Silent and immediate exit (no cleanup)
    except Exception:
        sys.exit(0)  # Fallback: graceful exit


