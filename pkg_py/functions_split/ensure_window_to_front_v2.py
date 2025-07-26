

def ensure_window_to_front_v2(window_title_seg=None, pid=None):
    import inspect
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.move_window_to_front_via_pid import move_window_to_front_via_pid
    from pkg_py.functions_split.ensure_window_to_front_core import ensure_window_to_front_core

    func_n = inspect.currentframe().f_code.co_name
    ensure_printed(f'''func_n={func_n} {'%%%FOO%%%' if LTA else ''}''')
    if window_title_seg:
        ensure_window_to_front_core(window_title_seg)
    elif pid is not None:
        move_window_to_front_via_pid(pid)
