from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.objects.pk_ttl_cache_manager import ensure_function_return_ttl_cached




@ensure_seconds_measured
# @ensure_function_return_ttl_cached(ttl_seconds=60, maxsize=64) # pk_option
def get_last_history(history_file):
    import os
    if os.path.exists(history_file):
        with open(history_file, encoding="utf-8") as f:
            return f.read().strip()
    return None
