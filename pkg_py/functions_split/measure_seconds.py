

def measure_seconds(func):
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from functools import wraps
    import inspect
    if not LTA:
        return func
    func_n = inspect.currentframe().f_code.co_name

    @wraps(func)
    def wrapper(*args, **kwargs):
        import time

        time_s = time.time()
        result = func(*args, **kwargs)  # 원래 함수 실행
        elapsed_seconds = time.time() - time_s
        # pk_colorama_init_once()
        ensure_printed(str_working=f"[ @{func_n} ] [ {func.__name__}() ]  elapsed_seconds={elapsed_seconds:.4f}",print_color='yellow')  # todo 'elapsed_seconds={elapsed_seconds:.4f}' 에 노랗게 해고 싶다.
        # todo : 통계자료 수집
        return result  # 원래 함수의 반환값 그대로 반환

    return wrapper
