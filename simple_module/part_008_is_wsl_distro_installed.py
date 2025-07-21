



from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_014_pk_print import pk_print


def is_wsl_distro_installed(wsl_distro_n):
    cmd = rf'wsl -l -v'
    std_list = cmd_to_os(cmd=cmd, encoding='utf-16')
    std_list = get_list_removed_by_removing_runtine(working_list=std_list)
    pk_print(rf'''type(lines) = "{type(std_list)}"''')
    pk_print(f'''lines = {std_list}''')
    pk_print(rf'''len(lines) = "{len(std_list)}"''')
    for line in std_list:
        if wsl_distro_n in line:
            pk_print(f'''"{wsl_distro_n} is installed"''', print_color="green")
            return 1
    pk_print(f'''"{wsl_distro_n} is not installed"''', print_color='red')
    return 0
