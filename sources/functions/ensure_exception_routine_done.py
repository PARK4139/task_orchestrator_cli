def ensure_exception_routine_done(*, __file__, traceback, exception=None):
    # TBD : ipdb 를 받을지 말지.
    from sources.functions.ensure_task_orchestrator_cli_log_editable import ensure_task_orchestrator_cli_log_editable
    import logging
    from sources.objects.pk_etc import PK_UNDERLINE
    from sources.functions.get_text_red import get_text_red
    from sources.objects.pk_local_test_activate import LTA

    # Lazy import to avoid circular dependency
    from sources.functions.ensure_debug_loged_simple import ensure_debug_loged_simple
    from sources.functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose

    PK_UNDERLINE = get_text_red(PK_UNDERLINE)

    logging.debug(PK_UNDERLINE)

    # log error cause
    ensure_debug_loged_simple(exception)  # logging.debug(rf"exception={exception}")
    logging.debug(PK_UNDERLINE)
    ensure_debug_loged_verbose(traceback)  # logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")

    # pk_option
    if not LTA:
        ensure_task_orchestrator_cli_log_editable()
    # ensure_task_orchestrator_cli_wrapper_suicided(__file__)
