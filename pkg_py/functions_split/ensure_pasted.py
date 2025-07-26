def ensure_pasted():
    from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    if is_os_wsl_linux():
        ensure_command_excuted_to_os('powershell.exe Get-Clipboard')
    else:
        import clipboard
        return clipboard.paste()
