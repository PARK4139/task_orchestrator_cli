def pk_paste():
    from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
    from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
    if is_os_wsl_linux():
        cmd_to_os('powershell.exe Get-Clipboard')
    else:
        import clipboard
        return clipboard.paste()
