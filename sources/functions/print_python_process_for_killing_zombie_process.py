

def print_python_process_for_killing_zombie_process():
    import inspect
    import psutil
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    for process in psutil.process_iter():
        print(rf'str(process.pid) : {str(process.pid)}')
        print(rf'process.status() : {process.status()}')
        print(rf'process.name() : {process.nick_name()}')
