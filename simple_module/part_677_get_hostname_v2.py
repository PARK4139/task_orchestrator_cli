from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os

from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os


def get_hostname_v2():
    hostname = cmd_to_os("hostname")[0]
    hostname = get_str_url_decoded(hostname)
    return hostname
