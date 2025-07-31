def ensure_snipping_tool_exe_opened():
    from pkg_py.functions_split.ensure_pressed import ensure_pressed
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.functions_split.is_os_linux import is_os_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.system_object.files import F_SNIPPING_TOOL_EXE
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.ensure_printed import ensure_printed

    if is_os_windows():
        # Windows에서는 explorer.exe로 실행
        ensure_command_excuted_to_os(cmd=fr"explorer.exe {F_SNIPPING_TOOL_EXE}")
        ensure_slept(milliseconds=100)
        ensure_pressed("ctrl", "n")
    elif is_os_linux():
        # Linux에서는 gnome-screenshot 사용
        ensure_command_excuted_to_os(cmd="gnome-screenshot --interactive")
        ensure_slept(milliseconds=100)
    else:
        # macOS나 다른 OS에서는 기본 스크린샷 도구 사용
        ensure_command_excuted_to_os(cmd="screenshot")
        ensure_slept(milliseconds=100)
