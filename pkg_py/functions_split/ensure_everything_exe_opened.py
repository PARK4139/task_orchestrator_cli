def ensure_everything_exe_opened():
    from pkg_py.system_object.files import F_EVERYTHING_EXE

    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    ensure_command_excuted_to_os(cmd=fr"explorer.exe {F_EVERYTHING_EXE}")
