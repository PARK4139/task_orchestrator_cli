from pkg_py.functions_split.ensure_remote_os_as_nopasswd import ensure_remote_os_as_nopasswd
from pkg_py.functions_split.ensure_ssh_public_key_to_remote_os import ensure_ssh_public_key_to_remote_os
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.pk_system_object.Local_test_activate import LTA


def assist_to_perform_to_ensure_vpc_condition():
    # todo:  request_template_raw 를 넣고 request 를 만들고 request 대로 셋팅 수행 ...하는 로직 파이프 고민필요

    import inspect

    func_n = inspect.currentframe().f_code.co_name

    if is_os_windows():
        # mkr_assist_to_perform_to_ensure_vpc_condition
        # todo guide_to_edit_vpc_config_script_and_update_toml        and        save to vpc_mamnagement_map_toml
        # todo : migrate hardcoding to get_from_toml # 현업에서는 협업을 위해서 필요.
        # 고정값은 migrate to toml and get from toml
        # 가변값은 guide
        f = F_VPC_MAMNAGEMENT_MAP_TOML

        # vpc data model orm (OBJECT RELATIONAL MAPPING)
        vpc_data_raw = get_vpc_data_raw_from_vpc_request()
        vpc_data = A2zCarDataStructure.RemoteDeviceDataStructure()
        vpc_data.set_remote_device_data_field_all(pk_structure=vpc_data_raw)
        vpc_data.print_remote_device_data_field_all(instance_name='vpc_data_defined')

        wsl_data_raw = get_wsl_data_raw_data(vpc_data_raw)
        wsl_data = A2zCarDataStructure.RemoteDeviceDataStructure()
        wsl_data.set_remote_device_data_field_all(pk_structure=wsl_data_raw)
        wsl_data.print_remote_device_data_field_all(instance_name='wsl_data')
        # [ how ] msi/wsl_ubuntu_24_04_no_flash/login.
        # msi

        ensure_wsl_distro_installed(wsl_distro_n=wsl_data.vpc_os_distro_n)
        ensure_wsl_distro_session(wsl_distro_n=wsl_data.vpc_os_distro_n)
        ensure_wsl_usb_ip_connection_established(wsl_distro_n=wsl_data.vpc_os_distro_n,
                                                 config_remote_os=config_remote_os)

        if vpc_data.vpc_ip:
            if LTA:
                pk_print(f'''vpc_data.ip={vpc_data.vpc_ip} {'%%%FOO%%%' if LTA else ''}''')
            config_remote_os = {}
            config_remote_os['ip'] = vpc_data.vpc_ip
            config_remote_os['local_ssh_private_key'] = vpc_data.vpc_local_ssh_private_key
            config_remote_os['port'] = vpc_data.vpc_port
            config_remote_os['user_n'] = vpc_data.vpc_user_n

            ensure_ssh_public_key_to_remote_os(**config_remote_os)
            ensure_remote_os_as_nopasswd(**config_remote_os)

        # argument 유효성 검사
        # pk_print(f'''ooo 과 ooo 이 초기화되지 않아 {vpc_identifier} 장비를 베이직 셋업과 스모크 테스트를 진행할 수 없습니다. {'%%%FOO%%%' if LTA else ''}''')
        # pk_print(f'''ooo a2z 외부차량탑재용으로 {vpc_identifier} 장비를 베이직 셋업과 스모크 테스트를 진행하시겠습니까? {'%%%FOO%%%' if LTA else ''}''')
        print_iterable_as_vertical(item_iterable=config_remote_os)
        raise

        ensure_vpc_ready(wsl_data=wsl_data, vpc_data=vpc_data, **config_remote_os)

        assist_to_ensure_vpc_bit(bit_mode='p')

        assist_to_ensure_vpc_bit(bit_mode='c')
