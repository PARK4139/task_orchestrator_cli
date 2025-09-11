def ensure_console_debuggable(ipdb=None):
    from sources.functions.ensure_slept import ensure_slept

    if ipdb is None:
        ensure_slept(hours=1, mode_countdown=0)  # task_orchestrator_cli_option
    else:
        ipdb.set_trace()  # task_orchestrator_cli_option # pk_fail
