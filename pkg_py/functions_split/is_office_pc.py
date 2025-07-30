from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
from pkg_py.functions_split.get_hostname import get_hostname


@ensure_seconds_measured
def is_pk_pc():
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_str_url_decoded import get_str_url_decoded
    hostname = get_hostname()
    hostname = get_str_url_decoded(hostname)
    ensure_printed(f"hostname={hostname}")
    if hostname in ["pk"]:
        return 1
    else:
        return 0
