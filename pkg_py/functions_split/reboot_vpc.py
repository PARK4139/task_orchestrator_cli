from pkg_py.pk_system_object.local_test_activate import LTA

from pkg_py.functions_split.pk_print import pk_print


def reboot_vpc(**config_remote_os):
    # stdout, stderr = cmd_to_remote_os(cmd = "sudo reboot",**config_remote_os)
    stdout, stderr = cmd_to_remote_os(cmd="sudo shutdown -r now", **config_remote_os)
    ip = config_remote_os['ip']
    while 1:
        if not ping(ip):
            pk_print(f'''ping ({ip}) {'%%%FOO%%%' if LTA else ''}''', print_color='green')
            return
        pk_sleep(milliseconds=20)
