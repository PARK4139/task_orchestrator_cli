

def back_up_pnx_list_biggest():
    from pkg_py.system_object.etc import BIGGEST_PNXS
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.compress_pnx_via_bz import compress_pnx_via_bz
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    ensure_printed(f"biggest_pnxs에 대한 백업을 시도합니다")
    for biggest_target in BIGGEST_PNXS:
        compress_pnx_via_bz(f'{biggest_target}')
