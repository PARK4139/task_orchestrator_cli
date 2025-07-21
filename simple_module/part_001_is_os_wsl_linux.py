

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist


def is_os_wsl_linux():
    # todo : detect wsl.exe

    if does_pnx_exist(pnx='/mnt/c/Users'):
        if LTA:
            pk_print(f'''wsl os is detected {'%%%FOO%%%' if LTA else ''}''')
        return 1
    else:
        return 0
