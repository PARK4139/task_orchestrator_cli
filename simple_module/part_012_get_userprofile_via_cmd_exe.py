



from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os


def get_userprofile_via_cmd_exe():
    userprofile = cmd_to_os("echo %USERPROFILE%")[0]
    userprofile = get_str_url_decoded(userprofile)
    return userprofile
