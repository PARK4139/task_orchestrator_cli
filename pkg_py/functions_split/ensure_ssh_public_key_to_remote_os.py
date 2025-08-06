

from pkg_py.system_object.local_test_activate import LTA
# pk_#
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_ssh_public_key_to_remote_os(**config_remote_os):
    import paramiko

    ip = config_remote_os['ip']
    port = config_remote_os['port']
    user_n = config_remote_os['user_n']
    pw = config_remote_os['pw']

    key_public = get_key_public(**config_remote_os)
    if check_ssh_server_public_key(key_public=key_public, **config_remote_os):
        ensure_printed("SSH PUBLIC KEY IS ALREADY REGISTERED")
        return
    else:
        ensure_printed(str_working="SSH PUBLIC KEY IS NOT REGISTERED", print_color='red')

    # Paramiko로 SSH 연결
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=ip, port=port, username=user_n, password=pw)
        ensure_printed(f"{'[ TRY GUIDE ]'} ssh -p {port} {user_n}@{ip} ")

        add_public_key_to_remote_via_paramiko(ssh_paramiko=ssh, key_public=key_public)

    except paramiko.AuthenticationException as e:
        ensure_printed(f"Authentication failed. Please check your user_n and password: {e}", print_color='red')
        raise
    except paramiko.SSHException as e:
        ensure_printed(f"SSH connection error: {e}", print_color='red')
        raise
    except Exception as e:
        ensure_printed(f"An unexpected error occurred: {e}", print_color='red')
        raise
    finally:
        ssh.close()
        if LTA:
            ensure_printed("SSH connection closed.")
