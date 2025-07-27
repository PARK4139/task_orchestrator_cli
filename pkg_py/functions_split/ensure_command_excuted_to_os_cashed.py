from pkg_py.system_object.ttl_cache_manager import ensure_function_ttl_cached


@ensure_function_ttl_cached(ttl_seconds=60, maxsize=64)
def ensure_command_excuted_to_os_cashed(cmd):
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    result = ensure_command_excuted_to_os(cmd=cmd)
    return result
