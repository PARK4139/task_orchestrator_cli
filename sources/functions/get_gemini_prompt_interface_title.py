from objects.pk_ttl_cache_manager import ensure_function_return_ttl_cached


@ensure_function_return_ttl_cached(ttl_seconds=60 * 1 * 1, maxsize=10)
def get_gemini_cli_assistance_title():
    return f"gemini_cli_whip"
