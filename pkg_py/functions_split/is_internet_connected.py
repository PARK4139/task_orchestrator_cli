from torch.fx.experimental.symbolic_shapes import lru_cache


@lru_cache(maxsize=10) # pk_options
def is_internet_connected():

    import inspect

    from pkg_py.functions_split.ensure_pinged import ensure_pinged

    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    from time import time

    func_n = inspect.currentframe().f_code.co_name

    if not hasattr(is_internet_connected, "_cache_time"):
        is_internet_connected._cache_time = 0
        is_internet_connected._cached_result = False

    now = time()
    if now - is_internet_connected._cache_time < 5:
        if LTA:
            ensure_printed(f"[USED] {func_n}() cache", print_color="green")
        return is_internet_connected._cached_result

    result = ensure_pinged(ip="8.8.8.8")
    if LTA:
        ensure_printed(f"[UPDATED] {func_n}() cache", print_color="green")

    is_internet_connected._cached_result = result
    is_internet_connected._cache_time = now
    return result
