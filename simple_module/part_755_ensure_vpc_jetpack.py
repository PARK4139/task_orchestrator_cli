from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def ensure_vpc_jetpack(**config_remote_os):
    # todo

    a, b = cmd_to_remote_os(cmd='todo', **config_remote_os)
    if 'Ubuntu' not in a:
        pk_print(f'''ubuntu is not installed({a}) {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        raise
