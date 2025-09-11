def ensure_job_offer_found():
    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.objects.task_orchestrator_cli_urls import URL_NAVER_MAIL, URL_GOOGLE_MAIL
    from sources.objects.task_orchestrator_cli_urls import URL_ALBAMON, URL_JOBKOREA, URL_SARAMIN
    ensure_command_executed(cmd=fr"explorer.exe {URL_SARAMIN}")
    ensure_command_executed(cmd=fr"explorer.exe {URL_JOBKOREA}")
    ensure_command_executed(cmd=fr"explorer.exe {URL_ALBAMON}")
    ensure_command_executed(cmd=fr"explorer.exe {URL_NAVER_MAIL}")
    ensure_command_executed(cmd=fr"explorer.exe {URL_GOOGLE_MAIL}")
