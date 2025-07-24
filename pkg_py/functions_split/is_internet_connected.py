import inspect


def is_internet_connected():
    func_n = inspect.currentframe().f_code.co_name
    from pkg_py.functions_split.ping import ping
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.system_object.local_test_activate import LTA
    from time import time
    if not hasattr(is_internet_connected, "_cache_time"):
        is_internet_connected._cache_time = 0
        is_internet_connected._cached_result = False

    now = time()
    if now - is_internet_connected._cache_time < 5:
        if LTA:
            pk_print(f"[USED] {func_n}() cache", print_color="green")
        return is_internet_connected._cached_result

    result = ping(ip="8.8.8.8")
    if LTA:
        pk_print(f"[UPDATED] {func_n}() cache", print_color="green")

    is_internet_connected._cached_result = result
    is_internet_connected._cache_time = now
    return result
