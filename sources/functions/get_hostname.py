from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_hostname():
    return get_hostname_v3()


def get_hostname_v1():
    from sources.functions.ensure_command_executed_like_human_as_admin import ensure_command_executed_like_human_as_admin

    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    lines = ensure_command_executed_like_human_as_admin('hostname')
    for line in lines:
        line = line.strip()
        return line


def get_hostname_v2():
    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.functions.get_str_url_decoded import get_str_url_decoded
    hostname = ensure_command_executed("hostname")[0]
    hostname = get_str_url_decoded(hostname)
    return hostname


def get_hostname_v3():
    from sources.functions.get_str_url_decoded import get_str_url_decoded
    import socket
    hostname = socket.gethostname()
    hostname = get_str_url_decoded(hostname)
    return hostname
