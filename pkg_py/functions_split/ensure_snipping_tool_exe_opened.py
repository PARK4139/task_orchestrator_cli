def ensure_snipping_tool_exe_opened():
    import inspect

    from pkg_py.functions_split.ensure_window_minimized import ensure_window_minimized
    from pkg_py.system_object.etc import pk_
    from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
    from pkg_py.functions_split.is_window_title_front import is_window_title_front
    from pkg_py.functions_split.ensure_pressed import ensure_pressed
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.functions_split.is_os_linux import is_os_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.system_object.files import F_SNIPPING_TOOL_EXE
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    func_n = inspect.currentframe().f_code.co_name
    if is_os_windows():
        ensure_command_excuted_to_os(cmd=fr"explorer.exe {F_SNIPPING_TOOL_EXE}")
        while True:
            # ensure_windows_printed()
            ensure_window_to_front(window_title_seg="캡처 도구")
            if is_window_title_front(window_title="캡처 도구"):
                ensure_window_minimized(window_title=f"{pk_}{func_n}")
                ensure_slept(milliseconds=100)
                ensure_pressed("ctrl", "n")
                return
            ensure_slept(milliseconds=100)

    elif is_os_linux():
        # Linux에서는 gnome-screenshot 사용
        ensure_command_excuted_to_os(cmd="gnome-screenshot --interactive")
        ensure_slept(milliseconds=100)
    else:
        # macOS나 다른 OS에서는 기본 스크린샷 도구 사용
        ensure_command_excuted_to_os(cmd="screenshot")
        ensure_slept(milliseconds=100)
