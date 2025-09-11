def set_wired_connection(vpc_wired_connection, **remote_device_target_config):
    from functions.ensure_command_to_remote_os import ensure_command_to_target
    from functions.get_str_from_list import get_str_from_list

    import logging
    cmd_list = []
    if target_device_wired_connection["address"] == "":
        cmd_list.append(
            f'sudo nmcli connection modify "Wired connection {vpc_wired_connection['wired_connection_no']}" ipv4.method "{vpc_wired_connection["method"]}"')
        cmd_list.append(
            f'sudo nmcli connection modify "Wired connection {vpc_wired_connection['wired_connection_no']}" ipv4.address "{vpc_wired_connection["address"]}"')
    else:
        cmd_list.append(
            f'sudo nmcli connection modify "Wired connection {vpc_wired_connection["wired_connection_no"]}" ipv4.address "{vpc_wired_connection["address"]}"')
        cmd_list.append(
            f'sudo nmcli connection modify "Wired connection {vpc_wired_connection["wired_connection_no"]}" ipv4.method "{vpc_wired_connection["method"]}"')
    cmd_list.append(
        f'sudo nmcli connection modify "Wired connection {vpc_wired_connection['wired_connection_no']}" ipv4.gateway "{vpc_wired_connection["gateway"]}"')
    cmd_list.append(
        f'sudo nmcli connection modify "Wired connection {vpc_wired_connection['wired_connection_no']}" ipv4.dns "{vpc_wired_connection["dns"]}"')
    for cmd in cmd_list:
        std_outs, std_err_list = ensure_command_to_target(cmd=cmd, **remote_device_target_config)
        std_err = get_str_from_list(working_list=std_err_list)
        if std_err:
            if "\n" in std_err:
                error_list = std_err.split("\n")
                for error_str in error_list:
                    logging.debug(f"{"[ ERROR ]"}{error_str}")
            else:
                logging.debug(f"{"[ ERROR ]"}{std_err}")
    ensure_command_to_target(cmd="sudo systemctl restart NetworkManager", **remote_device_target_config)
