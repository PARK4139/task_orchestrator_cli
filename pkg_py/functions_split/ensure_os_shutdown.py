def ensure_os_shutdown():
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    ensure_command_excuted_to_os(rf'%windir%\System32\Shutdown.exe -s ')
