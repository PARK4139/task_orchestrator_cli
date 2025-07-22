

from pkg_py.functions_split.pk_print import pk_print


def back_up_pnx_list_smallest():
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"smallest_pnxs에 대한 백업을 시도합니다")
    for target in SMALLEST_PNXS:
        compress_pnx_via_bz(f'{target}')
