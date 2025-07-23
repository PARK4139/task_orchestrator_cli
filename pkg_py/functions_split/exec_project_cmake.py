from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def exec_project_cmake(project_pnx, **config_remote_os):
    try:

        import traceback
        import sys
        import inspect
        func_n = inspect.currentframe().f_code.co_name
        ip = config_remote_os['ip']
        pw = config_remote_os['pw']
        port = config_remote_os['port']
        user_n = config_remote_os['user_n']
        local_ssh_public_key = config_remote_os['local_ssh_public_key']
        local_ssh_private_key = config_remote_os['local_ssh_private_key']

        cmd = rf"cd {project_pnx}/build && ./project_cmake"  # build 를 통해서 생성된 project_cmake exec  f 이다
        std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=cmd, **config_remote_os)
        cmd_to_remote_os_with_pubkey(cmd='sudo apt update', **config_remote_os)
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
