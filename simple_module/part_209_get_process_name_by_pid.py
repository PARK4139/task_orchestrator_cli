from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os


def get_process_name_by_pid(pid):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    try:
        data = cmd_to_os(cmd=f'tasklist | findstr "{pid}"')
        return data[0].split(" ")[0]
    except:
        return 0
