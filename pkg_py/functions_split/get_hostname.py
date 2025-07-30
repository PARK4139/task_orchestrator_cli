def get_hostname():
    from pkg_py.functions_split.get_hostname_v2 import get_hostname_v2

    # @ensure_seconds_measured
    # @ensure_function_ttl_cached(ttl_seconds=60, maxsize=64)  # pk_*
    # def _inner():
    #     return get_hostname_v2()

    # return _inner()
    return get_hostname_v2()
