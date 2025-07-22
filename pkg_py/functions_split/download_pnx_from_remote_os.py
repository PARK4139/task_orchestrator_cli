from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style


def download_pnx_from_remote_os(f_remote_src, f_local_dst, **config_remote_os):
    f_local_dst = get_pnx_os_style(f_local_dst)
    user = config_remote_os['user']
    ip = config_remote_os['ip']
    port = config_remote_os['port']
    cmd_to_remote_os(cmd=rf"scp -P {port} -r {user}@{ip}:{f_remote_src} {f_local_dst}", **config_remote_os)
