from objects.pk_ttl_cache_manager import ensure_function_return_ttl_cached
from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.objects.pk_local_test_activate import LTA

@ensure_seconds_measured
@ensure_function_return_ttl_cached(ttl_seconds=60 * 1 * 1, maxsize=10)
def get_gemini_installer_title():
    return "gemini_installer"