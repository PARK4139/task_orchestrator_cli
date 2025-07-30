def get_hostname_v2():
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.get_str_url_decoded import get_str_url_decoded
    hostname = ensure_command_excuted_to_os("hostname")[0]
    hostname = get_str_url_decoded(hostname)
    return hostname
