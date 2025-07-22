

# import win32process
# import win32gui


from pkg_py.pk_system_object.directories import D_PKG_TXT
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.pk_print import pk_print


def is_office_pc():
    hostname = cmd_to_os("hostname")[0]
    hostname = get_str_url_decoded(hostname)
    pk_print(f"hostname={hostname}")
    token_hostname_a2z_galaxybook = get_token_from_f_txt(f_token=rf'{D_PKG_TXT}\token_hostname_a2z_galaxybook.txt', initial_str="")
    token_hostname_home_desktop = get_token_from_f_txt(f_token=rf'{D_PKG_TXT}\token_hostname_home_desktop.txt', initial_str="")

    if hostname == token_hostname_home_desktop:
        return 0
    elif hostname == token_hostname_a2z_galaxybook:
        return 1
