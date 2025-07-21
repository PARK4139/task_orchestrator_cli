def get_nmcli_connection_list(**config_remote_os):
    std_out_list, std_err_list = cmd_to_remote_os(cmd=f'nmcli connection show', **config_remote_os)
    # std_out_list, std_err_list = cmd_to_remote_os(cmd=f'nmcli device status',**config_remote_os)
    return std_out_list, std_err_list
