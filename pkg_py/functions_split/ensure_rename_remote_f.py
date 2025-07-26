from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_rename_remote_f(remote_f_src, pnx_remote_d_dst, **config_remote_os):
    std_out_list, std_err_list = cmd_to_remote_os(cmd=f"mv {remote_f_src} {pnx_remote_d_dst}", **config_remote_os)
    if std_out_list == [] or std_err_list == []:
        ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''', print_color='green')
    else:
        ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
        raise
