from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.ensure_printed import ensure_printed


def reboot_vpc(**config_remote_os):
    # stdout, stderr = cmd_to_remote_os(cmd = "sudo reboot",**config_remote_os)
    stdout, stderr = cmd_to_remote_os(cmd="sudo shutdown -r now", **config_remote_os)
    ip = config_remote_os['ip']
    while 1:
        if not ensure_pinged(ip):
            ensure_printed(f'''ping ({ip}) {'%%%FOO%%%' if LTA else ''}''', print_color='green')
            return
        ensure_slept(milliseconds=20)
