

def print_python_process_for_killing_zombie_process():
    import inspect
    import psutil
    func_n = inspect.currentframe().f_code.co_name
    for process in psutil.process_iter():
        print(rf'str(process.pid) : {str(process.pid)}')
        print(rf'process.status() : {process.status()}')
        print(rf'process.name() : {process.name()}')
