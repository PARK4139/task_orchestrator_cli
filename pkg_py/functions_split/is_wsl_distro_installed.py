



from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_printed import ensure_printed


def is_wsl_distro_installed(wsl_distro_n):
    cmd = rf'wsl -l -v'
    std_list = cmd_to_os(cmd=cmd, encoding='utf-16')
    std_list = get_list_removed_by_removing_runtine(working_list=std_list)
    ensure_printed(rf'''type(lines) = "{type(std_list)}"''')
    ensure_printed(f'''lines = {std_list}''')
    ensure_printed(rf'''len(lines) = "{len(std_list)}"''')
    for line in std_list:
        if wsl_distro_n in line:
            ensure_printed(f'''"{wsl_distro_n} is installed"''', print_color="green")
            return 1
    ensure_printed(f'''"{wsl_distro_n} is not installed"''', print_color='red')
    return 0
