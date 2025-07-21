

def get_vpc_processer_name_via_scp(vpc_data_raw):
    config_remote_os = {}
    config_remote_os['ip'] = vpc_data_raw.vpc_ip
    config_remote_os['port'] = vpc_data_raw.vpc_port
    config_remote_os['user_n'] = vpc_data_raw.vpc_user_n
    config_remote_os['local_ssh_private_key'] = vpc_data_raw.vpc_local_ssh_private_key
    config_remote_os['local_ssh_public_key'] = vpc_data_raw.vpc_local_ssh_public_key
    std_out_list, std_err_list = cmd_to_remote_os(cmd='ifconfig', **config_remote_os)
