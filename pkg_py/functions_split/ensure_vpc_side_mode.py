from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.directories import D_PKG_TXT
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def ensure_vpc_side_mode(vpc_data, config_remote_os):
    import traceback

    import os

    vpc_side_mode = vpc_data.vpc_side_mode
    vpc_aifw_version = vpc_data.vpc_aifw_version
    with_packing_mode = vpc_data.with_packing_mode

    # ip_after_flash = config_remote_os['ip']
    # pw = config_remote_os['pw']
    # port = config_remote_os['port']
    # user_n = config_remote_os['user_n']
    # local_ssh_public_key = config_remote_os['local_ssh_public_key']

    # vpc_type = get_vpc_type()
    ip_new = get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_vpc_{vpc_side_mode}_side.toml', initial_str="")
    try:
        # cmd = "mkdir -p ~/.ssh && chmod 700 ~/.ssh"
        # std_out_list, std_err_list = cmd_to_remote_os(cmd=cmd, **config_remote_os)
        # if std_out_list != [] or std_err_list != []:
        #     return

        ensure_remove_and_make_remote_d(d='~/works', **config_remote_os)

        d_temp = make_and_get_d_temp()

        config_aidev1_release_server = {
            'user_n': get_token_from_f_token(f_token=rf'{D_PKG_TXT}\user_gitlab_token.txt', initial_str=""),
            'ip': get_token_from_f_token(f_token=rf'{D_PKG_TXT}\ip_gitlab_token.txt', initial_str=""),
            'pw': get_token_from_f_token(f_token=rf'{D_PKG_TXT}\pw_gitlab_token.txt', initial_str=""),
            'port': get_token_from_f_token(f_token=rf'{D_PKG_TXT}\port_gitlab_token.txt', initial_str=""),
        }
        download_pnx_from_aidev1_release_server(
            remote_f_src=f"/home/user/release/remote_release_{vpc_aifw_version}.zip", local_d_dst=d_temp,
            **config_aidev1_release_server)

        upload_pnx_to_remote_os(local_pnx_src=f'{d_temp}/remote_release_{vpc_aifw_version}.zip',
                                remote_pnx_dst=f'/home/nvidia/works/remote_release_{vpc_aifw_version}.zip',
                                **config_remote_os)

        ensure_pnx_removed(d_temp)

        ensure_unzip_remote_f(remote_f_src=f'~/works/remote_release_{vpc_aifw_version}.zip', pnx_remote_d_dst='~/works',
                              **config_remote_os)

        ensure_rename_remote_f(remote_f_src=f'~/works/remote_release_{vpc_aifw_version}',
                               pnx_remote_d_dst='~/works/remote_release', **config_remote_os)

        d_temp = make_and_get_d_temp()

        # download f (a2z_xavier_launcher)
        os.chdir(d_temp)
        std_list = ensure_command_excuted_to_os(
            cmd="git clone -b packing_ai_framework --single-branch http://211.171.108.170:8003/ai_dept/a2z_xavier_launcher.git")

        # send f (a2z_xavier_launcher)
        upload_pnx_to_remote_os(local_pnx_src=os.path.join(d_temp, f'a2z_xavier_launcher'),
                                remote_pnx_dst='/home/nvidia/works', **config_remote_os)

        ensure_pnx_removed(d_temp)

        # unzip f (a2z_xavier_launcher)
        cmd = f"unzip -o ~/works/a2z_xavier_launcher.zip -d ~/works/a2z_xavier_launcher"
        std_out_list, std_err_list = cmd_to_remote_os(cmd=cmd, **config_remote_os)
        if std_out_list == [] or std_err_list == []:
            ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''', print_color='green')
        else:
            ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
            raise

        d_temp = make_and_get_d_temp()

        # download xc_field.sh
        os.chdir(d_temp)
        f_remote_src = rf"{d_temp}/xc_field.sh"
        f_remote_src = get_pnx_unix_style(f_remote_src)
        f_nx = get_nx(f_remote_src)
        token_gitlab_repo = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\token_xc_field_gitlab_repo.txt',
                                                   initial_str=rf"")
        download_f_from_gitlab(f_nx_remote_src='xc_field.sh', d_local_dst=d_temp, gitlab_repo_url=token_gitlab_repo)

        # edit xc_field.sh
        # todo : chore : No password / ai_framework model packing ver / a2z_xavier_launcher / IP Setting
        # 이것도 자동화 하자
        f_remote_src = get_pnx_windows_style(f_remote_src)
        ensure_command_excuted_to_os(rf' explorer "{f_remote_src}" ')
        check_manual_task_iteractively(
            question=rf'''did you finish customizing {f_nx} manually?  {'%%%FOO%%%' if LTA else ''}''',
            ignore_uppercase_word_list=[f_nx])

        # remove xc_field.sh
        cmd = f"rm -rf ~/{f_nx}"
        std_out_list, std_err_list = cmd_to_remote_os_with_pw_via_paramiko(cmd=cmd, **config_remote_os)
        if std_out_list == [] or std_err_list == []:
            ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''', print_color='green')
        else:
            ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
            return

        # send xc_field.sh
        upload_pnx_to_remote_os(local_pnx_src=os.path.join(d_temp, f'{f_nx}'), remote_pnx_dst=f'/home/nvidia/{f_nx}',
                                **config_remote_os)

        # xc_field.sh chmod
        cmd = f"chmod +x ~/{f_nx}"
        std_out_list, std_err_list = cmd_to_remote_os_with_pw_via_paramiko(cmd=cmd, **config_remote_os)
        if std_out_list == [] or std_err_list == []:
            ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''', print_color='green')
        else:
            ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
            return

        # import ipdb
        # ipdb.set_trace()

        cmd = f"echo '{pw}' | sudo -S bash -c \"echo 'nvidia ALL=(ALL:ALL) NOPASSWD:ALL' >> /etc/sudoers\""
        std_out_list, std_err_list = cmd_to_remote_os_with_pw_via_paramiko(cmd=cmd, **config_remote_os)
        cmd = "sudo grep -n 'nvidia ALL=(ALL:ALL) NOPASSWD:ALL' /etc/sudoers"
        std_out_list, std_err_list = cmd_to_remote_os_with_pw_via_paramiko(cmd=cmd, **config_remote_os)
        # echo 'nvidia ALL=(ALL:ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/nvidia
        # sudo chmod 440 /etc/sudoers.d/nvidia
        if "nvidia ALL=(ALL:ALL) NOPASSWD:ALL" in std_out_list:
            ensure_printed("THE ENTRY IS ALREADY PRESENT.", 'green')
        else:
            import ipdb
            ipdb.set_trace()

        # visudo 등록상태 검사
        cmd = f"sudo visudo -c"
        std_out_list, std_err_list = cmd_to_remote_os_with_pw_via_paramiko(cmd=cmd, **config_remote_os)
        if "parsed OK" not in std_out_list:
            ensure_printed(str_working=rf'''{cmd} fail  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

        # a2z_xavier_launcher.zip rm
        cmd = f"rm -rf ~/works/a2z_xavier_launcher.zip"
        std_out_list, std_err_list = cmd_to_remote_os_with_pw_via_paramiko(cmd=cmd, **config_remote_os)
        if std_out_list == [] or std_err_list == []:
            ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''', print_color='green')
        else:
            ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
            return

        # set xc_field.sh {mode}
        cmd = f"~/{f_nx} {vpc_side_mode}"
        cmd_to_remote_os(cmd=cmd, **config_remote_os)

        check_manual_task_iteractively(question=rf'''did {f_nx} works successfully?  {'%%%FOO%%%' if LTA else ''}''')

        check_manual_task_iteractively(question=rf'''did exit {f_nx} at local?  {'%%%FOO%%%' if LTA else ''}''')

        # remove xc_field.sh
        cmd = f"rm -rf ~/{f_nx}"
        std_out_list, std_err_list = cmd_to_remote_os_with_pw_via_paramiko(cmd=cmd, **config_remote_os)
        if std_out_list == [] or std_err_list == []:
            ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''', print_color='green')
        else:
            ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
            return

        # download xc_field.sh
        f_remote_src = rf"{d_temp}/xc_field.sh"
        f_remote_src = get_pnx_unix_style(f_remote_src)
        f_nx = get_nx(f_remote_src)
        token_gitlab_repo = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\token_xc_field_gitlab_repo.txt',
                                                   initial_str=rf"")
        download_f_from_gitlab(f_nx_remote_src='xc_field.sh', d_local_dst=d_temp, gitlab_repo_url=token_gitlab_repo)
        if not does_pnx_exist(pnx=f_remote_src):
            ensure_pnx_removed(d_temp)
            ensure_pnx_made(pnx=d_temp, mode='d')
            os.chdir(d_temp)
            token_gitlab_repo = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\token_xc_field_gitlab_repo.txt',
                                                       initial_str=rf"")
            download_f_from_gitlab(f_nx_remote_src='xc_field.sh', d_local_dst=d_temp, gitlab_repo_url=token_gitlab_repo)
        if not does_pnx_exist(pnx=f_remote_src):
            ensure_printed(str_working=rf'''{f_remote_src} does not exist.  {'%%%FOO%%%' if LTA else ''}''',
                     print_color='red')
            import ipdb
            ipdb.set_trace()
            return

        # transfer xc_field.sh
        f_local_src = os.path.join(d_temp, f'{f_nx}')
        f_remote_dst = f'/home/nvidia/{f_nx}'
        upload_pnx_to_remote_os(local_pnx_src=f_local_src, remote_pnx_dst=f_remote_dst, **config_remote_os)

        # ip = get_ip_choosen_by_user_input_via_available_ip()  # todo : ref : 불필요해보임.
        # ip = '192.168.10.114'  # todo : code for dev
        ip_new = None
        if vpc_side_mode == 'a':
            ip_new = get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_vpc_a_side.toml', initial_str=""),
        elif vpc_side_mode == 'b':
            ip_new = get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_vpc_b_side.toml', initial_str=""),

        # debug
        # stdout, stderr = get_wired_connection_list_via_paramiko(port=port_xc, users=users_xc, ip=ip, pw=pw_xc)

        # reset
        reset_wired_connection_list(wired_connection_no_range=range(1, 5), **config_remote_os)

        # set as mode
        set_wired_connection(vpc_data.wired_connection_1_new, **config_remote_os)
        set_wired_connection(vpc_data.wired_connection_3_new, **config_remote_os)

        # set as custom
        # wired_connection_no = 3
        # set_wired_connection_via_paramiko( port=port_xc, users=users_xc, ip=ip, pw=pw_xc, wired_connection_info={"address": rf"192.168.2.114/22", "method": "manual", "gateway": "192.168.1.1", "dns": "8.8.8.8", })
        # set_wired_connection_via_paramiko( port=port_xc, users=users_xc, ip=ip, pw=pw_xc, wired_connection_info={"address": rf"192.168.10.114/24", "method": "manual", "gateway": "", "dns": "", })

        print_wired_connection_list(wired_connection_no_range=range(1, 5), config_remote_os=config_remote_os)

        # 원격 시스템 reboot
        reboot_vpc()

        check_manual_task_iteractively(question=f'''DID THE AI FRAMEWORK WORK AFTER THE OS OF THE vpc WAS REBOOTED?''')

        # todo : chore : System Settings... 등, 현재의 XC flash 이미지는 문제가 없음.
        # ensure_printed(f'''check "System Settings..."''', print_color='blue')
        # input(rf"{get_stamp_func_n(func_n=func_n)} >")

        ensure_pnx_removed(d_temp)

        ensure_printed(str_working=rf'''Successfully, set XC as {vpc_side_mode}.  {'%%%FOO%%%' if LTA else ''}''',
                 print_color="green")
    except:
        ensure_printed(str_working=rf"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''} ", print_color='red')
        import sys
        raise
