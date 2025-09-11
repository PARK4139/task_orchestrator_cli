def is_internet_connected():
    import inspect

    from sources.functions.ensure_pinged import ensure_pinged

    import logging
    from sources.objects.pk_local_test_activate import LTA
    from time import time

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    if not hasattr(is_internet_connected, "_cache_time"):
        is_internet_connected._cache_time = 0
        is_internet_connected._cached_result = False

    now = time()
    if now - is_internet_connected._cache_time < 5:
        if LTA:
            logging.debug(f"[USED] {func_n}() cache")
        return is_internet_connected._cached_result

    result = ensure_pinged(ip="8.8.8.8")
    if LTA:
        logging.debug(f"[UPDATED] {func_n}() cache")

    is_internet_connected._cached_result = result
    is_internet_connected._cache_time = now
    return result
