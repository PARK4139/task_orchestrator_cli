from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_api_usage_allowed(api_key_id):
    from sources.functions import ensure_value_completed
    from sources.objects.pk_map_texts import PkTexts

    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.objects.task_orchestrator_cli_urls import URL_OPEN_API_USAGE_DASHBOARD

    if api_key_id == "OPENAI_API":
        ensure_command_executed(cmd=fr"explorer.exe {URL_OPEN_API_USAGE_DASHBOARD}")

    question = rf"are you sure {api_key_id} usage proper"
    decision = ensure_value_completed(key_hint=rf"{question}=", options=[PkTexts.YES, PkTexts.NO])
    if decision == PkTexts.YES:
        return True
    else:
        return False


