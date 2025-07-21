

# import win32process
# import win32gui

from pkg_py.simple_module.part_014_pk_print import pk_print

# deep size 측정용 (optional, pip install pympler)

try:
    from pympler import asizeof

    have_pympler = True
except ImportError:
    have_pympler = False


def pk_measure_memory(func):
    import psutil

    #

    import functools
    import os
    import sys

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        # 강제 가비지 컬렉션 후 초기 메모리 측정 (선택)
        # import gc; gc.collect()
        before_rss = proc.memory_info().rss
        result = func(*args, **kwargs)
        # import gc; gc.collect()
        after_rss = proc.memory_info().rss
        delta_rss_mb = (after_rss - before_rss) / (1024 ** 2)

        # 반환 객체 크기 측정 (얕은 크기)
        shallow_bytes = sys.getsizeof(result)
        shallow_mb = shallow_bytes / (1024 ** 2)

        msg = (f"[{func.__name__}] RSS 증가: {delta_rss_mb:.2f} MiB, "
               f"반환 객체 얕은 크기: {shallow_mb:.2f} MiB")

        # deep 크기 측정 (가능한 경우)
        if have_pympler:
            deep_bytes = asizeof.asizeof(result)
            deep_mb = deep_bytes / (1024 ** 2)
            msg += f", 반환 객체 깊은 크기: {deep_mb:.2f} MiB"
        else:
            msg += " (deep 측정하려면 `pip install pympler`)"

        pk_print(msg, print_color="yellow")
        return result

    return wrapper
