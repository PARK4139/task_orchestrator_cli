



from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os


def get_userprofile_via_cmd_exe():
    userprofile = ensure_command_excuted_to_os("echo %USERPROFILE%")[0]
    userprofile = get_str_url_decoded(userprofile)
    return userprofile
