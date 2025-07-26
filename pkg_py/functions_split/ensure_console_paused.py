def ensure_console_paused():
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    # input(f"PAUSED BY {func_n}(), IF YOU WANT TO GO, PRESS ANY KEY")
    input(f"PAUSED, IF YOU WANT TO GO, PRESS ANY KEY")
