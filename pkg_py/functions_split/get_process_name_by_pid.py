from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os


def get_process_name_by_pid(pid):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    try:
        data = ensure_command_excuted_to_os(cmd=f'tasklist | findstr "{pid}"')
        return data[0].split(" ")[0]
    except:
        return 0
