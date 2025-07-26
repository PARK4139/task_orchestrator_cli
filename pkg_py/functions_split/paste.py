def paste():
    from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
    from pkg_py.functions_split.cmd_to_os import cmd_to_os
    if is_os_wsl_linux():
        cmd_to_os('powershell.exe Get-Clipboard')
    else:
        import clipboard
        return clipboard.paste()
