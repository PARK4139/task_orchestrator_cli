

# import pywin32
# import pywin32
# from project_database.test_project_database import MySqlUtil


from pkg_py.pk_system_object.directories import D_DOWNLOADS
from pkg_py.functions_split.cmd_to_os import cmd_to_os

from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style


def move_pnx_from_remote_os_to_local(pnx, d_dst=None, **config_remote_os):
    # todo

    pnx = get_pnx_unix_style(pnx)
    ip = config_remote_os['ip']
    port = config_remote_os['port']
    user_n = config_remote_os['user_n']
    d_dst = d_dst or D_DOWNLOADS
    d_dst = get_pnx_unix_style(d_dst)
    cmd_to_os(cmd=f'scp -P {port} -r {user_n}@{ip}:"{pnx}" "{d_dst}"')
    pk_sleep(milliseconds=500)
