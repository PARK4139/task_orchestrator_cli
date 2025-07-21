

def ensure_window_to_front(window_title_seg=None, pid=None):
    from pkg_py.pk_system_layer_100_Local_test_activate import LTA
    from pkg_py.simple_module.part_014_pk_print import pk_print
    from pkg_py.simple_module.part_589_check_min_non_null_or_warn import check_min_non_null_or_warn
    from pkg_py.simple_module.part_592_ensure_window_to_front_v2 import ensure_window_to_front_v2
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    pk_print(f'''func_n={func_n} {'%%%FOO%%%' if LTA else ''}''')
    if not check_min_non_null_or_warn(window_title_seg, pid, func_n=func_n, arg_none_required=1):
        # raise
        return
    # ensure_window_to_front_v0(window_title_seg=window_title_seg, pid=pid)
    # ensure_window_to_front_v1(window_title_seg=window_title_seg, pid=pid)
    ensure_window_to_front_v2(window_title_seg=window_title_seg, pid=pid)
