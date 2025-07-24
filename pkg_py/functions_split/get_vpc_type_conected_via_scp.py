from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def get_vpc_type_conected_via_scp(vpc_data_raw):
    # todo : jetson_setup identify.py 참고
    # todo : processer name    core cnt    로 vpc 특징을 판단

    return 'no'

    config_remote_os = {}
    config_remote_os['ip'] = vpc_data_raw.vpc_ip
    config_remote_os['port'] = vpc_data_raw.vpc_port
    config_remote_os['user_n'] = vpc_data_raw.vpc_user_n
    config_remote_os['local_ssh_private_key'] = vpc_data_raw.vpc_local_ssh_private_key

    vpc_type = None
    vpc_ip = config_remote_os['ip']

    vpc_core_cnt_of_evm = 8
    vpc_core_cnt_of_xc = 8
    vpc_core_cnt_of_nx = 8
    vpc_core_cnt_of_no = 8
    vpc_processser_name_of_evm = 'todo'
    vpc_processser_name_of_xc = 'todo'
    vpc_processser_name_of_nx = 'todo'
    vpc_processser_name_of_no = 'todo'
    # vpc_current_upper_limit =
    # vpc_power_upper_limit =
    # vpc_cpu_clock_upper_limit =

    vpc_identifier_and_vpc_nvidia_serial_map_dict = get_vpc_identifier_and_vpc_nvidia_serial_map()
    for vpc_nvidia_serial, vpc_identifier in vpc_identifier_and_vpc_nvidia_serial_map_dict.items():
        if vpc_nvidia_serial != vpc_data_raw.vpc_nvidia_serial:
            continue
        elif vpc_nvidia_serial == vpc_data_raw.vpc_nvidia_serial:
            vpc_type = vpc_nvidia_serial.split(f"{PK_BLANK}#")[0]
            return vpc_type
        else:
            pk_print(str_working=rf'''unkown exception.  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            raise

    vpc_core_cnt = vpc_data_raw.vpc_core_cnt
    processer_name_of_remote_os = vpc_data_raw.vpc_proceser_name
    if vpc_core_cnt == vpc_core_cnt_of_no and processer_name_of_remote_os == vpc_processser_name_of_no:
        vpc_type = 'no'
    elif vpc_core_cnt == vpc_core_cnt_of_nx and processer_name_of_remote_os == vpc_processser_name_of_nx:
        vpc_type = 'nx'
    elif vpc_core_cnt == vpc_core_cnt_of_xc and processer_name_of_remote_os == vpc_processser_name_of_xc:
        vpc_type = 'xc'
    elif vpc_core_cnt == vpc_core_cnt_of_evm and processer_name_of_remote_os == vpc_processser_name_of_evm:
        vpc_type = 'evm'
    else:
        pk_print(
            str_working=rf'''unkown vpc_type (vpc_ip={vpc_ip}, vpc_core_cnt={vpc_core_cnt}, processer_name_of_remote_os={processer_name_of_remote_os} ).  {'%%%FOO%%%' if LTA else ''}''',
            print_color='red')
        raise
    return vpc_type.lower()
