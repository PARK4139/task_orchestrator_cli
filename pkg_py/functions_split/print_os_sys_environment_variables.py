from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical


def print_os_sys_environment_variables():
    import os
    import ipdb
    print_iterable_as_vertical(item_iterable=os.environ, item_iterable_n='모든 시스템 환경변수 출력')

    ipdb.set_trace()
