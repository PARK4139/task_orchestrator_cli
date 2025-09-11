from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.objects.pk_ttl_cache_manager import ensure_function_return_ttl_cached


@ensure_seconds_measured
@ensure_function_return_ttl_cached(ttl_seconds=60 * 1 * 1, maxsize=10) # task_orchestrator_cli_option
def get_gemini_version_installed():
    from sources.functions.ensure_command_executed import ensure_command_executed
    std_list = ensure_command_executed("gemini --version")
    return std_list
