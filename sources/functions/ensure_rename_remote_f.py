from sources.objects.pk_local_test_activate import LTA
import logging


def ensure_rename_remote_f(remote_f_src, pnx_remote_d_dst, **remote_device_target_config):
    std_outs, std_err_list = ensure_command_to_remote_os(cmd=f"mv {remote_f_src} {pnx_remote_d_dst}", **remote_device_target_config)
    if std_outs == [] or std_err_list == []:
        logging.debug(f'''{'%%%FOO%%%' if LTA else ''}''')
    else:
        logging.debug(rf'''{'%%%FOO%%%' if LTA else ''}''')
        raise
