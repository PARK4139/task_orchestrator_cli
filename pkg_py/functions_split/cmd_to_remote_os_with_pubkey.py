


# from pkg_py.system_object.is_os_windows import is_os_windows

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def cmd_to_remote_os_with_pubkey(cmd, **config_remote_os):
    try:
        import paramiko

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 호스트 키 자동 수락

        if not does_pnx_exist(pnx=config_remote_os['local_ssh_private_key']):  # todo local_ssh_private_key 가 path 라면 f_ prefix 추가.
            ensure_printed(f'''config_remote_os['local_ssh_private_key']={config_remote_os['local_ssh_private_key']} {'%%%FOO%%%' if LTA else ''}''')
            state = is_os_windows()
            ensure_state_printed(state=state, pk_id="%%%FOO%%%")
            if state:
                ensure_command_excuted_to_os(f'ssh-keygen -t ed25519 -b 4096 -C "pk_ssh_key"')
            else:
                ensure_command_excuted_to_os(f'ssh-keygen -t ed25519 -C "pk_ssh_key"')
        key_private = paramiko.Ed25519Key(filename=config_remote_os['local_ssh_private_key'])

        ensure_printed(f'''config_remote_os['user_n']={config_remote_os['user_n']} {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''config_remote_os['ip']={config_remote_os['ip']} {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''config_remote_os['port']={config_remote_os['port']} {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''key_private={key_private} {'%%%FOO%%%' if LTA else ''}''')

        if not config_remote_os['ip']:
            ensure_printed(f'''config_remote_os['ip'] is None {'%%%FOO%%%' if LTA else ''}''')
            return None, None

        ssh.connect(hostname=config_remote_os['ip'], port=config_remote_os['port'], username=config_remote_os['user_n'], pkey=key_private)

        # The authenticity of host 'todo' can't be established.
        # ED25519 key fingerprint is SHA256:kO5qGJ92luOdRTm1Ye4pycNnXbNV4sl8gSoB9dAp9Uc.
        # This key is not known by any other names.

        std_out_list = []
        std_err_list = []

        # cmd_with_sudo_s = f"sudo -S {cmd}"
        cmd_with_sudo_s = f"{cmd}"
        ensure_printed(f'''{STAMP_REMOTE_DEBUG} cmd={cmd}  {'%%%FOO%%%' if LTA else ''}''')
        stdin, stdout, stderr = ssh.exec_command(cmd_with_sudo_s)

        stdout_str = stdout.read().decode()
        stderr_str = stderr.read().decode()

        if stdout_str:
            std_out_list = stdout_str.split("\n")
        if stderr_str:
            std_err_list = stderr_str.split("\n")

        for std_out_str in std_out_list:
            ensure_printed(f'''{STAMP_REMOTE_DEBUG} {std_out_str} {'%%%FOO%%%' if LTA else ''}''', print_color='green')

        if len(std_out_list) > 0 and len(std_err_list) > 0:
            # std_out_list 가 std_err_list 모두 있는 경우는 성공했지만 warning 을 띄우는 경우이다. 이 경우는 std_err_list 는 [] 로 초기화 처리했다
            for std_err_str in std_err_list:
                ensure_printed(f'''{STAMP_REMOTE_ERROR} {std_err_str} {'%%%FOO%%%' if LTA else ''}''', print_color='yellow')
            std_err_list = []
            if LTA:
                ensure_printed(f'''std_out_list={std_out_list} {'%%%FOO%%%' if LTA else ''}''')
                ensure_printed(f'''std_err_list={std_err_list} {'%%%FOO%%%' if LTA else ''}''')

            return std_out_list, std_err_list
        else:
            for std_err_str in std_err_list:
                ensure_printed(f'''{STAMP_REMOTE_ERROR} {std_err_str} {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            if LTA:
                ensure_printed(f'''std_out_list={std_out_list} {'%%%FOO%%%' if LTA else ''}''')
                ensure_printed(f'''std_err_list={std_err_list} {'%%%FOO%%%' if LTA else ''}''')
            return std_out_list, std_err_list

    except Exception as e:
        import traceback
        ensure_printed(str_working=rf"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''} ", print_color='red')
