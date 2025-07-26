from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_vpc_ip(vpc_data, **config_remote_os):
    vpc_ip = vpc_data.vpc_ip
    vpc_side_mode = vpc_data.vpc_side
    vpc_type = vpc_data.vpc_type
    vpc_identifier = vpc_data.vpc_identifier
    ip_new = vpc_data.vpc_ip
    while 1:
        set_vpc_ip(vpc_data, **config_remote_os)
        if not ping(ip_new):
            ensure_printed(str_working=rf'''{vpc_type} set as {vpc_side_mode} side {'%%%FOO%%%' if LTA else ''}''',
                     print_color="red")
            raise
        else:
            break
