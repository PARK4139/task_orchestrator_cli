from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def ensure_unzip_remote_f(remote_f_src, pnx_remote_d_dst, **config_remote_os):
    std_out_list, std_err_list = cmd_to_remote_os(cmd=f"unzip {remote_f_src} -d {pnx_remote_d_dst}", **config_remote_os)
    if std_out_list == [] or std_err_list == []:
        pk_print(f'''{'%%%FOO%%%' if LTA else ''}''', print_color='green')
    else:
        pk_print(working_str=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
        raise
