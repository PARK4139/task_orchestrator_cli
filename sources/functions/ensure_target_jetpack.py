from sources.objects.pk_local_test_activate import LTA
import logging


def ensure_target_jetpack(**remote_device_target_config):
    # todo

    a, b = ensure_command_to_remote_os(cmd='todo', **remote_device_target_config)
    if 'Ubuntu' not in a:
        logging.debug(f'''ubuntu is not installed({a}) {'%%%FOO%%%' if LTA else ''}''')
        raise
