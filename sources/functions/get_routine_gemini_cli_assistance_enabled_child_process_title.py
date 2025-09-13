from sources.objects.pk_ttl_cache_manager import ensure_function_return_ttl_cached


@ensure_function_return_ttl_cached(ttl_seconds=60 * 1 * 1, maxsize=10)
def get_routine_gemini_cli_assistance_enabled_child_process_title():
    # return rf"routine_gemini_cli_assistance_enabled_child_process"
    return rf"ensure_routine_gemini_cli_assistance_enabled.py_child_process"
