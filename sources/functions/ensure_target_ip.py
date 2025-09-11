from sources.objects.pk_local_test_activate import LTA
import logging


def ensure_target_ip (target_device_data, **remote_device_target_config):
    target_device_ip = target_device_data.target_device_ip
    target_device_side_mode = target_device_data.target_device_side
    target_device_type = target_device_data.target_device_type
    target_device_identifier = target_device_data.device_identifier
    ip_new = target_device_data.target_device_ip
    while 1:
        set_target_ip (target_device_data, **remote_device_target_config)
        if not ensure_pinged(ip_new):
            logging.debug(rf'''{vpc_type} set as {vpc_side_mode} side {'%%%FOO%%%' if LTA else ''}''')
            raise
        else:
            break
