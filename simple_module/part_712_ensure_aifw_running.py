

def ensure_aifw_running(vpc_data, config_remote_os):
    if vpc_data.vpc_type == 'no':
        while 1:
            if not is_aifw_docker_container_running():
                run_vpc_aifw_docker_container(vpc_data, config_remote_os)
                if is_aifw_docker_container_running():
                    break
    elif vpc_data.vpc_type == 'nx':
        # cd ~/works/ai_framework/bin
        # ./a2z_component_front_launcher cfg_pack_merge_front.cfg
        # ./a2z_component_merge_launcher cfg_pack_merge_front.cfg
        pass
    elif vpc_data.vpc_type == 'xc':
        # exec ai_framework
        # vscode/Remote Explorer/SSH/192.168.2.114/~/works/ai_framework/bin
        # vscode/Remote Explorer/SSH/192.168.2.114/~/works/ai_framework/bin ./a2z_component_front_launcher cfg_pack_merge_front.cfg
        # vscode/Remote Explorer/SSH/192.168.2.114/~/works/ai_framework/bin ./a2z_component_merge_launcher cfg_pack_merge_front.cfg
        pass
