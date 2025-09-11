from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_history_file_pnx_return(file_id):
    from sources.objects.task_orchestrator_cli_directories import D_HISTORY_CACHE
    from sources.functions.does_pnx_exist import is_pnx_existing
    import logging
    from sources.objects.pk_local_test_activate import LTA

    from sources.functions.ensure_pnx_made import ensure_pnx_made

    history_file = D_HISTORY_CACHE / f"{file_id}.history"
    logging.debug(f'''history_file={history_file} {'%%%FOO%%%' if LTA else ''}''')
    ensure_pnx_made(pnx=history_file, mode="f")
    return history_file
