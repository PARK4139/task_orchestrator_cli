from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.pk_print import pk_print


def download_pnx_from_aidev1_release_server(remote_f_src, local_d_dst, **config_aidev1_release_server):
    import paramiko
    import os

    user_n = config_aidev1_release_server['user_n']
    ip = config_aidev1_release_server['ip']
    pw = config_aidev1_release_server['pw']
    port = config_aidev1_release_server['port']

    # todo 보안고민필요...ssh public key 저장해도 되는지..안되면 로컬에 다운받아 넣는 식으로...보안 트집 잡히지 말고 자동화 수립
    # todo migrate secret txt f to token

    remote_f_src = get_pnx_unix_style(remote_f_src)
    pk_print(str_working=rf'''src="{remote_f_src}"  {'%%%FOO%%%' if LTA else ''}''')

    f_dst = rf"{local_d_dst}/{get_nx(remote_f_src)}"
    f_dst = get_pnx_windows_style(f_dst)
    pk_print(f'''f_dst={f_dst} {'%%%FOO%%%' if LTA else ''}''')

    ssh = None
    sftp = None
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=user_n, password=pw)

        sftp = ssh.open_sftp()

        d_local = os.path.dirname(f_dst)
        if not os.path.exists(d_local):
            os.makedirs(d_local)

        pk_print(f"started to download pnx {remote_f_src} to {f_dst}")
        sftp.get(remote_f_src, f_dst)
        pk_print(f"download pnx {f_dst}", print_color='green')

    except paramiko.AuthenticationException:
        pk_print("ssh Authentication failed. Please check your user_n and pw.", print_color='red')
        raise
    except Exception as e:
        pk_print(f"Error: {e}", print_color='red')
        raise
    finally:
        if sftp:
            sftp.close()
        if ssh:
            ssh.close()
        if LTA:
            pk_print("SSH connection closed.")
