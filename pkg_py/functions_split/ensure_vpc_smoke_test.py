from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def ensure_vpc_smoke_test(vpc_data):
    import traceback

    import os

    import inspect
    # IT에서 XC로 docker image전송
    # IT에서 XC로 docker image run 명령
    # IT에서 XC에서 제어PC로 결과 수집

    func_n = inspect.currentframe().f_code.co_name

    vpc_aifw_version = vpc_data.vpc_aifw_version
    vpc_id = vpc_data.vpc_id
    vpc_side_mode = vpc_data.vpc_side
    vpc_type = vpc_data.vpc_type

    # 초기 설정 및 유효성 검사

    config_remote_os = {}
    config_remote_os['ip'] = get_ip_available_by_user_input()
    config_remote_os['pw'] = vpc_data.vpc_pw
    config_remote_os['port'] = vpc_data.vpc_port
    config_remote_os['user_n'] = vpc_data.vpc_user_n
    config_remote_os['local_ssh_public_key'] = os.path.join(D_HOME, ".ssh", "id_ed25519.pub")

    ensure_ssh_public_key_to_remote_os(**config_remote_os)

    # 임시 _d_ 설정
    d_temp = make_and_get_d_temp()

    check_manual_task_iteractively(
        question=rf'''did you verify lan6 connected and indicator is dimming ?  {'%%%FOO%%%' if LTA else ''}''')
    if not ensure_vpc_ip(vpc_data, **config_remote_os):
        ip = get_ip_available_by_user_input()

    # input(f"{pk_get_colorful_str_working_with_stamp_enviromnet(func_n=func_n)} >")  # [SUGGEST] sleep() 하는게 어떤가?

    ensure_auto_reboot_test()

    try:
        # set_remote_os_as_nopasswd_v1(**config_remote_os)
        ensure_remote_os_as_nopasswd(**config_remote_os)

        # remove f remote (vpc_info_collector.sh)
        f_nx = 'vpc_info_collector.sh'
        std_out_list, std_err_list = cmd_to_remote_os(cmd=f"rm -rf ~/Downloads/{f_nx}", **config_remote_os)
        if std_out_list == [] or std_err_list == []:
            ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''', print_color='green')
        else:
            ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
            raise

        # send f (vpc_info_collector.sh)
        f_nx = 'vpc_info_collector.sh'
        f_local = os.path.join(D_PROJECT_VSTEST, f_nx)
        f_remote = os.path.join('/home/nvidia/Downloads', f_nx)
        upload_pnx_to_remote_os(local_pnx_src=f_local, remote_pnx_dst=f_remote, **config_remote_os)

        # chmod +x (vpc_info_collector.sh)
        cmd = rf"chmod +x {f_remote}"
        std_out_list, std_err_list = cmd_to_remote_os(cmd=cmd, **config_remote_os)
        if std_out_list != [] or std_err_list != []:
            return

        # run f (vpc_info_collector.sh)
        cmd = rf"cd {get_p(f_remote)} && {f_remote}"
        # cmd = rf"{remote_f}"
        std_out_list, std_err_list = cmd_to_remote_os(cmd=cmd, **config_remote_os)
        if std_out_list == [] or std_err_list == []:
            ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''', print_color='green')
        else:
            ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
            return

        vpc_id = vpc_id.strip()
        yymmdd = get_yymmdd()

        # download f (vpc_info_collector.txt)
        f_remote_src = "/home/nvidia/Downloads/vpc_info_collector.txt"
        f_local_new = rf"{D_PROJECT_VSTEST}/{vpc_id}_smoke_test_report_at_{yymmdd}.txt"
        download_pnx_from_remote_os(f_remote_src, f_local_new, **config_remote_os)

        # check f_local_dst
        f_local_new = get_pnx_os_style(f_local_new)
        if does_pnx_exist(pnx=f_local_new):
            ensure_command_excuted_to_os(cmd=f'explorer "{f_local_new}" ', mode='a')

        # convert from lf to crlf # todo for not working
        f_n = get_n(f_nx)
        f_x = get_x(f_nx)
        f_to = rf"{D_PROJECT_VSTEST}/{f_n}_crlf{f_x}"
        f_to = get_pnx_windows_style(f_to)
        convert_lf_to_crlf(f_from=f_local_new, f_to=f_to)

        # convert from binary to txt
        # f_from = f_to
        # f_to = rf"{PROJECT_DIRECTORY}/{f_n}_binary{f_x}"
        # convert_binary_to_text(binary_f=f_from, txt_f=f_to)

        # rename vpc_info_collector.txt
        f_remote_src = "/home/nvidia/Downloads/vpc_info_collector.txt"
        f_remote_new = f'/home/nvidia/Downloads/{vpc_id}_smoke_test_report_at_{yymmdd}.txt'
        std_out_list, std_err_list = cmd_to_remote_os(cmd=f"mv {f_remote_src} {f_remote_new}", **config_remote_os)
        if std_out_list == [] or std_err_list == []:
            ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''', print_color='green')
        else:
            ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
            return

        # remove vpc_info_collector.sh
        std_out_list, std_err_list = cmd_to_remote_os(cmd=f"rm -rf ~/Downloads/vpc_info_collector.sh",
                                                      **config_remote_os)
        if std_out_list == [] or std_err_list == []:
            ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''', print_color='green')
        else:
            ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
            return

        # compare vpc tree
        vpc_aifw_version = vpc_aifw_version.replace('.', "_")
        f_vpc_ref_tree2 = rf"{D_PROJECT_VSTEST}\{get_n(f_to)}_tree_{yymmdd}.toml"
        f_vpc_tree_answer = rf"{D_PROJECT_VSTEST}/{vpc_type}_{vpc_aifw_version}_tree_{vpc_side_mode}_ref.toml"
        save_vpc_tree_to_f_toml(f=f_vpc_ref_tree2, config_remote_os=config_remote_os)
        ignore_list = [
            "/home/nvidia/.local",
            # "/home/nvidia/.compiz",
            "/home/nvidia/.cache",
            "/home/nvidia/works/log",
            "/home/nvidia/works/a2z_xavier_launcher/log",
            "/home/nvidia/.ssh/known_hosts",
            "/home/nvidia/.config",
        ]
        compare_vpc_tree(f_vpc_tree_answer_list=f_vpc_tree_answer, f_vpc_ref_tree2_list=f_vpc_ref_tree2,
                         ignore_list=ignore_list)

        ensure_pnx_removed(d_temp)

        import ipdb
        ipdb.set_trace()

        print_wired_connection_list(wired_connection_no_range=range(1, 5), **config_remote_os)

        reset_wired_connection_list(wired_connection_no_range=range(1, 5), **config_remote_os)

        # set vpc ip
        ensure_vpc_ip(vpc_data, **config_remote_os)

        # input(f"{pk_get_colorful_str_working_with_stamp_enviromnet(func_n=func_n)} >")

        # set vpc ip as custom
        wired_connection_3_new = {'wired_connection_no': 3, "address": rf"", "method": "auto", "gateway": "",
                                  "dns": ""}  # reset vpc ip
        wired_connection_3_new = {'wired_connection_no': 3, "address": rf"192.168.2.124/22", "method": "manual",
                                  "gateway": "192.168.1.1", "dns": "8.8.8.8"}
        wired_connection_3_new = {'wired_connection_no': 3, "address": rf"192.168.2.114/22", "method": "manual",
                                  "gateway": "192.168.1.1", "dns": "8.8.8.8"}
        wired_connection_3_new = {'wired_connection_no': 3, "address": rf"192.168.10.114/22", "method": "manual",
                                  "gateway": "", "dns": ""}
        set_wired_connection(wired_connection_3_new, **config_remote_os)

        # if xc
        # a2z_component_f, a2z_component_m %CPU 확인
        # 카메라 미연결 시, a2z_component_f, %CPU=100~110
        cmd_to_remote_os(cmd=f"top", **config_remote_os)

        # cmd = f"sudo dmesg"
        cmd_to_remote_os(cmd=f"sudo dmesg -w", **config_remote_os)

        cmd_to_remote_os(cmd=f"timedatectl", **config_remote_os)

        # 로거 설정확인
        cmd_to_remote_os(cmd=f"cat ./autorun.sh", **config_remote_os)

        # 로거 테스트
        # a2z_xavier_launcher.zip
        std_out_list, std_err_list = cmd_to_remote_os(
            cmd=f"cd ~/works/a2z_wavier_launcher && sudo python3 SystemLogger.py", **config_remote_os)
        if std_out_list == [] or std_err_list == []:
            ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''', print_color='green')
        else:
            ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
            return

        # 로그 확인
        # find /home/nvidia/works/log/ -ctime +4 -delete

        # 로그 수집

        # 강제전원remove 후 재부팅 시 AI_Framework 동작여부 확인 테스트
        check_manual_task_iteractively(question=rf'''remove power of XC, forcely ? {'%%%FOO%%%' if LTA else ''}''')
        check_manual_task_iteractively(question=rf'''connect power of XC, again ? {'%%%FOO%%%' if LTA else ''}''')
        check_manual_task_iteractively(
            question=rf'''AI frame work is restarted, again ? {'%%%FOO%%%' if LTA else ''}''')

    except:
        ensure_printed(str_working=rf"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''} ", print_color='red')
        return
    finally:
        ensure_pnx_removed(d_temp)
