from sources.objects.pk_ttl_cache_manager import ensure_function_return_ttl_cached


@ensure_function_return_ttl_cached(ttl_seconds=60, maxsize=64)
def ensure_command_executed_cashed(cmd):
    from sources.functions.ensure_command_executed import ensure_command_executed
    result = ensure_command_executed(cmd=cmd)
    return result
