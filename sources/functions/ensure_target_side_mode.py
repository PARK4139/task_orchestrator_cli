from sources.objects.pk_local_test_activate import LTA
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.functions.get_nx import get_nx
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
import logging
from sources.functions.does_pnx_exist import is_pnx_existing


def ensure_target_side_mode (target_device_data, remote_device_target_config):
    import traceback

    import os

    target_device_side_mode = target_device_data.target_device_side_mode
    target_device_aifw_version = target_device_data.target_device_aifw_version
    with_packing_mode = target_device_data.with_packing_mode

    # ip_after_flash = remote_device_target_config['ip']
    # pw = remote_device_target_config['pw']
    # port = remote_device_target_config['port']
    # user_n = remote_device_target_config['user_n']
    # local_ssh_public_key = remote_device_target_config['local_ssh_public_key']

    # target_device_type = get_target_type()
    ip_new = get_pk_token(f_token=rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/pk_token_ip_target_{vpc_side_mode}_side.toml', initial_str="")
    try:
        # cmd = "mkdir -p ~/.ssh && chmod 700 ~/.ssh"
        # std_outs, std_err_list = ensure_command_to_remote_os(cmd=cmd, **remote_device_target_config)
        # if std_outs != [] or std_err_list != []:
        #     return

        ensure_remove_and_make_remote_d(d='~/works', **remote_device_target_config)

        d_temp = make_and_get_d_temp()

        config_aidev1_ensure_release_server_ran = {
            'user_n': get_token_from_f_token(f_token=rf'{D_PK_RECYCLE_BIN}\user_gitlab_token.txt', initial_str=""),
            'ip': get_token_from_f_token(f_token=rf'{D_PK_RECYCLE_BIN}\ip_gitlab_token.txt', initial_str=""),
            'pw': get_token_from_f_token(f_token=rf'{D_PK_RECYCLE_BIN}\pw_gitlab_token.txt', initial_str=""),
            'port': get_token_from_f_token(f_token=rf'{D_PK_RECYCLE_BIN}\port_gitlab_token.txt', initial_str=""),
        }
        download_pnx_from_aidev1_ensure_release_server_ran(
            remote_f_src=f"/home/user/release/remote_release_{vpc_aifw_version}.zip", local_d_dst=d_temp,
            **config_aidev1_ensure_release_server_ran)

        upload_pnx_to_remote_os(local_pnx_src=f'{d_temp}/remote_release_{vpc_aifw_version}.zip',
                                remote_pnx_dst=f'/home/nvidia/works/remote_release_{vpc_aifw_version}.zip',
                                **remote_device_target_config)

        ensure_pnx_removed(d_temp)

        ensure_unzip_remote_f(remote_f_src=f'~/works/remote_release_{vpc_aifw_version}.zip', pnx_remote_d_dst='~/works',
                              **remote_device_target_config)

        ensure_rename_remote_f(remote_f_src=f'~/works/remote_release_{vpc_aifw_version}',
                               pnx_remote_d_dst='~/works/remote_release', **remote_device_target_config)

        d_temp = make_and_get_d_temp()

        # download f (TBD_xavier_launcher)
        os.chdir(d_temp)
        std_list = ensure_command_executed(
            cmd="git clone -b packing_ai_framework --single-branch http://211.171.108.170:8003/ai_dept/TBD_xavier_launcher.git")

        # send f (TBD_xavier_launcher)
        upload_pnx_to_remote_os(local_pnx_src=os.path.join(d_temp, f'TBD_xavier_launcher'),
                                remote_pnx_dst='/home/nvidia/works', **remote_device_target_config)

        ensure_pnx_removed(d_temp)

        # unzip f (TBD_xavier_launcher)
        cmd = f"unzip -o ~/works/TBD_xavier_launcher.zip -d ~/works/TBD_xavier_launcher"
        std_outs, std_err_list = ensure_command_to_remote_os(cmd=cmd, **remote_device_target_config)
        if std_outs == [] or std_err_list == []:
            logging.debug(f'''{'%%%FOO%%%' if LTA else ''}''')
        else:
            logging.debug(rf'''{'%%%FOO%%%' if LTA else ''}''')
            raise

        d_temp = make_and_get_d_temp()

        # download xc_field.sh
        os.chdir(d_temp)
        f_remote_src = rf"{d_temp}/xc_field.sh"
        f_remote_src = get_pnx_unix_style(f_remote_src)
        f_nx = get_nx(f_remote_src)
        token_gitlab_repo = get_token_from_f_token(f_token=rf'{D_PK_RECYCLE_BIN}\token_xc_field_gitlab_repo.txt',
                                                   initial_str=rf"")
        download_f_from_gitlab(f_nx_remote_src='xc_field.sh', d_local_dst=d_temp, gitlab_repo_url=token_gitlab_repo)

        # edit xc_field.sh
        # todo : chore : No password / ai_framework model packing ver / TBD_xavier_launcher / IP Setting
        # 이것도 자동화 하자
        f_remote_src = get_pnx_windows_style(f_remote_src)
        ensure_command_executed(rf' explorer "{f_remote_src}" ')
        check_manual_task_iteractively(
            question=rf'''did you finish customizing {f_nx} manually?  {'%%%FOO%%%' if LTA else ''}''',
            ignore_uppercase_word_list=[f_nx])

        # remove xc_field.sh
        cmd = f"rm -rf ~/{f_nx}"
        std_outs, std_err_list = ensure_command_to_remote_os_with_pw_via_paramiko(cmd=cmd, **remote_device_target_config)
        if std_outs == [] or std_err_list == []:
            logging.debug(f'''{'%%%FOO%%%' if LTA else ''}''')
        else:
            logging.debug(rf'''{'%%%FOO%%%' if LTA else ''}''')
            return

        # send xc_field.sh
        upload_pnx_to_remote_os(local_pnx_src=os.path.join(d_temp, f'{f_nx}'), remote_pnx_dst=f'/home/nvidia/{f_nx}',
                                **remote_device_target_config)

        # xc_field.sh chmod
        cmd = f"chmod +x ~/{f_nx}"
        std_outs, std_err_list = ensure_command_to_remote_os_with_pw_via_paramiko(cmd=cmd, **remote_device_target_config)
        if std_outs == [] or std_err_list == []:
            logging.debug(f'''{'%%%FOO%%%' if LTA else ''}''')
        else:
            logging.debug(rf'''{'%%%FOO%%%' if LTA else ''}''')
            return

        # import ipdb
        # ipdb.set_trace()

        cmd = f"echo '{pw}' | sudo -S bash -c \"echo 'nvidia ALL=(ALL:ALL) NOPASSWD:ALL' >> /etc/sudoers\""
        std_outs, std_err_list = ensure_command_to_remote_os_with_pw_via_paramiko(cmd=cmd, **remote_device_target_config)
        cmd = "sudo grep -n 'nvidia ALL=(ALL:ALL) NOPASSWD:ALL' /etc/sudoers"
        std_outs, std_err_list = ensure_command_to_remote_os_with_pw_via_paramiko(cmd=cmd, **remote_device_target_config)
        # echo 'nvidia ALL=(ALL:ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/nvidia
        # sudo chmod 440 /etc/sudoers.d/nvidia
        if "nvidia ALL=(ALL:ALL) NOPASSWD:ALL" in std_outs:
            logging.debug("THE ENTRY IS ALREADY PRESENT.", 'green')
        else:
            import ipdb
            ipdb.set_trace()

        # visudo 등록상태 검사
        cmd = f"sudo visudo -c"
        std_outs, std_err_list = ensure_command_to_remote_os_with_pw_via_paramiko(cmd=cmd, **remote_device_target_config)
        if "parsed OK" not in std_outs:
            logging.debug(rf'''{cmd} fail  {'%%%FOO%%%' if LTA else ''}''')

        # TBD_xavier_launcher.zip rm
        cmd = f"rm -rf ~/works/TBD_xavier_launcher.zip"
        std_outs, std_err_list = ensure_command_to_remote_os_with_pw_via_paramiko(cmd=cmd, **remote_device_target_config)
        if std_outs == [] or std_err_list == []:
            logging.debug(f'''{'%%%FOO%%%' if LTA else ''}''')
        else:
            logging.debug(rf'''{'%%%FOO%%%' if LTA else ''}''')
            return

        # set xc_field.sh {mode}
        cmd = f"~/{f_nx} {vpc_side_mode}"
        ensure_command_to_remote_os(cmd=cmd, **remote_device_target_config)

        check_manual_task_iteractively(question=rf'''did {f_nx} works successfully?  {'%%%FOO%%%' if LTA else ''}''')

        check_manual_task_iteractively(question=rf'''did exit {f_nx} at local?  {'%%%FOO%%%' if LTA else ''}''')

        # remove xc_field.sh
        cmd = f"rm -rf ~/{f_nx}"
        std_outs, std_err_list = ensure_command_to_remote_os_with_pw_via_paramiko(cmd=cmd, **remote_device_target_config)
        if std_outs == [] or std_err_list == []:
            logging.debug(f'''{'%%%FOO%%%' if LTA else ''}''')
        else:
            logging.debug(rf'''{'%%%FOO%%%' if LTA else ''}''')
            return

        # download xc_field.sh
        f_remote_src = rf"{d_temp}/xc_field.sh"
        f_remote_src = get_pnx_unix_style(f_remote_src)
        f_nx = get_nx(f_remote_src)
        token_gitlab_repo = get_token_from_f_token(f_token=rf'{D_PK_RECYCLE_BIN}\token_xc_field_gitlab_repo.txt',
                                                   initial_str=rf"")
        download_f_from_gitlab(f_nx_remote_src='xc_field.sh', d_local_dst=d_temp, gitlab_repo_url=token_gitlab_repo)
        if not is_pnx_existing(pnx=f_remote_src):
            ensure_pnx_removed(d_temp)
            ensure_pnx_made(pnx=d_temp, mode='d')
            os.chdir(d_temp)
            token_gitlab_repo = get_token_from_f_token(f_token=rf'{D_PK_RECYCLE_BIN}\token_xc_field_gitlab_repo.txt',
                                                       initial_str=rf"")
            download_f_from_gitlab(f_nx_remote_src='xc_field.sh', d_local_dst=d_temp, gitlab_repo_url=token_gitlab_repo)
        if not is_pnx_existing(pnx=f_remote_src):
            logging.debug(rf'''{f_remote_src} does not exist.  {'%%%FOO%%%' if LTA else ''}''')
            import ipdb
            ipdb.set_trace()
            return

        # transfer xc_field.sh
        f_local_src = os.path.join(d_temp, f'{f_nx}')
        f_remote_dst = f'/home/nvidia/{f_nx}'
        upload_pnx_to_remote_os(local_pnx_src=f_local_src, remote_pnx_dst=f_remote_dst, **remote_device_target_config)

        # ip = get_ip_choosen_by_user_input_via_available_ip()  # todo : ref : 불필요해보임.
        # ip = '192.168.10.114'  # todo : code for dev
        ip_new = None
        if target_device_side_mode == 'a':
            ip_new = get_pk_token(f_token=rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/pk_token_ip_target_a_side.toml', initial_str=""),
        elif target_device_side_mode == 'b':
            ip_new = get_pk_token(f_token=rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/pk_token_ip_target_b_side.toml', initial_str=""),

        # debug
        # stdout, stderr = get_wired_connection_list_via_paramiko(port=port_xc, users=users_xc, ip=ip, pw=pw_xc)

        # reset
        reset_wired_connection_list(wired_connection_no_range=range(1, 5), **remote_device_target_config)

        # set as mode
        set_wired_connection (target_device_data.wired_connection_1_new, **remote_device_target_config)
        set_wired_connection (target_device_data.wired_connection_3_new, **remote_device_target_config)

        # set as custom
        # wired_connection_no = 3
        # set_wired_connection_via_paramiko( port=port_xc, users=users_xc, ip=ip, pw=pw_xc, wired_connection_info={"address": rf"192.168.2.114/22", "method": "manual", "gateway": "192.168.1.1", "dns": "8.8.8.8", })
        # set_wired_connection_via_paramiko( port=port_xc, users=users_xc, ip=ip, pw=pw_xc, wired_connection_info={"address": rf"192.168.10.114/24", "method": "manual", "gateway": "", "dns": "", })

        print_wired_connection_list(wired_connection_no_range=range(1, 5), remote_device_target_config=remote_device_target_config)

        # 원격 시스템 reboot
        reboot_vpc()

        check_manual_task_iteractively(question=f'''DID THE AI FRAMEWORK WORK AFTER THE OS OF THE target_device WAS REBOOTED?''')

        # todo : chore : System Settings... 등, 현재의 XC flash 이미지는 문제가 없음.
        # logging.debug(f'''check "System Settings..."''')
        # input(rf"{get_stamp_func_n(func_n=func_n)} >")

        ensure_pnx_removed(d_temp)

        logging.debug(rf'''Successfully, set XC as {vpc_side_mode}.  {'%%%FOO%%%' if LTA else ''}''')
    except:
        logging.debug(rf"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''} ")
        import sys
        raise
