from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def build_project_cmake(project_pnx, **config_remote_os):
    try:

        import traceback

        import inspect

        func_n = inspect.currentframe().f_code.co_name

        ip = config_remote_os['ip']
        pw = config_remote_os['pw']
        port = config_remote_os['port']
        user_n = config_remote_os['user_n']
        local_ssh_public_key = config_remote_os['local_ssh_public_key']
        local_ssh_private_key = config_remote_os['local_ssh_private_key']

        cmd = "cmake --version"
        std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=cmd, **config_remote_os)
        if not len(std_err_list) == 0:
            for std_err_str in std_err_list:
                pk_print(working_str=rf'{STAMP_REMOTE_ERROR} {std_err_str}', print_color='red')
            return
        if not len(std_out_list) == 0:
            for std_out_str in std_out_list:
                pk_print(working_str=rf'{STAMP_REMOTE_DEBUG} {std_out_str}')
                prompt_positive = "cmake version "
                if prompt_positive in std_out_str:
                    break

        cmd = rf"rm -rf {project_pnx}/build"
        std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=cmd, **config_remote_os)
        if not len(std_err_list) == 0:
            for std_err_str in std_err_list:
                pk_print(working_str=rf'{STAMP_REMOTE_ERROR} {std_err_str}', print_color='red')
            return
        if not len(std_out_list) == 0:
            for std_out_str in std_out_list:
                pk_print(working_str=rf'{STAMP_REMOTE_DEBUG} {std_out_str}')

        cmd = rf"mkdir -p {project_pnx}/build"
        std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=cmd, **config_remote_os)
        if not len(std_err_list) == 0 and not len(std_out_list) == 0:
            return

        cmd = rf"cd {project_pnx}/build && cmake .."
        std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=cmd, **config_remote_os)
        if not len(std_err_list) == 0:
            for std_err_str in std_err_list:
                pk_print(working_str=rf'{STAMP_REMOTE_ERROR} {std_err_str}', print_color='red')

            # [ TRY GUIDE ] : sudo apt install build-essential cmake g++ make git libyaml-cpp-dev

            # cmd = rf"sudo apt update"
            # std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(ip=ip, port=port, username=username, local_ssh_private_key=local_ssh_private_key, cmd=cmd)
            # if not len(std_err_list) == 0:
            #     for std_err_str in std_err_list:
            #         pk_print(str_working=rf'{STAMP_REMOTE_ERROR} {std_err_str}', print_color='red')
            #     return
            # if not len(std_out_list) == 0:
            #     for std_out_str in std_out_list:
            #         pk_print(str_working=rf'{STAMP_REMOTE_DEBUG} {std_out_str}')

            # cmd = rf"sudo apt install build-essential cmake g++ make git libyaml-cpp-dev"
            # std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(ip=ip, port=port, username=username, local_ssh_private_key=local_ssh_private_key, cmd=cmd)
            # if not len(std_err_list) == 0:
            #     for std_err_str in std_err_list:
            #         pk_print(str_working=rf'{STAMP_REMOTE_ERROR} {std_err_str}', print_color='red')
            #     return
            # if not len(std_out_list) == 0:
            #     for std_out_str in std_out_list:
            #         pk_print(str_working=rf'{STAMP_REMOTE_DEBUG} {std_out_str}')

            return
        if not len(std_out_list) == 0:
            for std_out_str in std_out_list:
                pk_print(working_str=rf'{STAMP_REMOTE_DEBUG} {std_out_str}')

        cmd = rf"cd {project_pnx}/build && make"
        std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=cmd, **config_remote_os)
        if not len(std_err_list) == 0:
            for std_err_str in std_err_list:
                pk_print(working_str=rf'{STAMP_REMOTE_ERROR} {std_err_str}', print_color='red')
            return
        if not len(std_out_list) == 0:
            for std_out_str in std_out_list:
                pk_print(working_str=rf'{STAMP_REMOTE_DEBUG} {std_out_str}')

        pk_print(working_str=rf'''{func_n}()  {'%%%FOO%%%' if LTA else ''}''', print_color='green')
    except:
        pk_print(working_str=rf"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''} ", print_color='red')
        raise
