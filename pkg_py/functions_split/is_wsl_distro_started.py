



from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_printed import ensure_printed


def is_wsl_distro_started(wsl_distro_n):
    cmd = rf'wsl -l -v'
    std_list = cmd_to_os(cmd=cmd, encoding='utf-16')
    std_list = get_list_removed_by_removing_runtine(working_list=std_list)
    signiture = wsl_distro_n
    signiture2 = 'Running'
    for line in std_list:
        if signiture in line:
            if signiture2 in line:
                if LTA:
                    ensure_printed(f'''{wsl_distro_n} is started in wsl {'%%%FOO%%%' if LTA else ''}''', print_color='green')
                return 1
    return 0
