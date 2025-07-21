from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style


def upload_pnx_to_remote_os(local_pnx_src, remote_pnx_dst, **config_remote_os):
    local_pnx_src = get_pnx_unix_style(local_pnx_src)
    remote_pnx_dst = get_pnx_unix_style(remote_pnx_dst)
    if is_f(local_pnx_src):
        send_f_to_remote_os(f_local_src=local_pnx_src, f_remote_dst=remote_pnx_dst, **config_remote_os)
    elif is_d(local_pnx_src):
        send_d_to_remote_os(d_local_src=local_pnx_src, d_remote_dst=remote_pnx_dst, **config_remote_os)
