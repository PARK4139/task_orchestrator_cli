from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def ensure_vpc_ip(vpc_data, **config_remote_os):
    vpc_ip = vpc_data.vpc_ip
    vpc_side_mode = vpc_data.vpc_side
    vpc_type = vpc_data.vpc_type
    vpc_identifier = vpc_data.vpc_identifier
    ip_new = vpc_data.vpc_ip
    while 1:
        set_vpc_ip(vpc_data, **config_remote_os)
        if not ping(ip_new):
            pk_print(working_str=rf'''{vpc_type} set as {vpc_side_mode} side {'%%%FOO%%%' if LTA else ''}''',
                     print_color="red")
            raise
        else:
            break
