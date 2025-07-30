def ensure_SnippingTool_exe_opened():
    from pkg_py.functions_split.ensure_pressed import ensure_pressed
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.system_object.files import F_SNIPPING_TOOL_EXE

    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    ensure_command_excuted_to_os(cmd=fr"explorer.exe {F_SNIPPING_TOOL_EXE}")
    ensure_slept(milliseconds=100)
    ensure_pressed("ctrl", "n")
