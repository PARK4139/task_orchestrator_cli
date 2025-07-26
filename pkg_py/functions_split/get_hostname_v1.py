

def get_hostname_v1():
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    lines = ensure_command_excuted_to_os_like_person_as_admin('hostname')
    for line in lines:
        line = line.strip()
        return line
