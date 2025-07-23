

def remove_vpc_aifw(vpc_data, config_remote_os):
    if vpc_data.vpc_type == 'no':
        # remote os 가 docker 여도 가능한지 모르겠다.
        # * 넣을지 말지 판단필요
        cmd_to_remote_os(cmd='rm -rf ~/Workspace/ai_framework*', **config_remote_os)
