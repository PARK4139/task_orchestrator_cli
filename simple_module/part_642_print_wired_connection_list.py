from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical


def print_wired_connection_list(config_remote_os, wired_connection_no_range):
    import re
    ensure_ubuntu_pkg_to_remote_os(ubuntu_pkg_n='net-tools', **config_remote_os)

    for wired_connection_no in wired_connection_no_range:
        stdout_list = []

        # 한 번만 호출하여 전체 정보를 가져오기
        cmd = f"sudo nmcli connection show 'Wired connection {wired_connection_no}'"
        std_out_list, std_err_list = cmd_to_remote_os(cmd=cmd, **config_remote_os)

        # list to str
        std_out = get_str_from_list(working_list=std_out_list)

        # parse
        ipv4_address = re.search(r'ipv4.addresses\s*:\s*([\d\.\/]+)', std_out)  # 수정된 정규식
        ipv4_method = re.search(r'ipv4.method\s*:\s*(\S+)', std_out)
        ipv4_gateway = re.search(r'ipv4.gateway\s*:\s*(\S+)', std_out)
        ipv4_dns = re.search(r'ipv4.dns\s*:\s*(\S+)', std_out)

        # None filter
        not_parsed = "(not parsed)"
        ipv4_address = ipv4_address.group(1) if ipv4_address else not_parsed
        ipv4_method = ipv4_method.group(1) if ipv4_method else not_parsed
        ipv4_gateway = ipv4_gateway.group(1) if ipv4_gateway else not_parsed
        ipv4_dns = ipv4_dns.group(1) if ipv4_dns else not_parsed

        # strip() filter
        ipv4_address = ipv4_address.strip()
        ipv4_method = ipv4_method.strip()
        ipv4_gateway = ipv4_gateway.strip()
        ipv4_dns = ipv4_dns.strip()

        # add to list
        stdout_list.append(f"___________________________________________________________")
        if not_parsed in ipv4_address:
            stdout_list.append(f"{not_parsed}")
        else:
            stdout_list.append(f"ipv4.address: {ipv4_address}")
            stdout_list.append(f"ipv4.method: {ipv4_method}")
            stdout_list.append(f"ipv4.gateway: {ipv4_gateway}")
            stdout_list.append(f"ipv4.dns: {ipv4_dns}")
        stdout_list.append(f"___________________________________________________________")

        # 수직으로 출력
        print_iterable_as_vertical(item_iterable=stdout_list, item_iterable_n=f"Wired connection {wired_connection_no}")
