

def gather_pnxs_empty_at_tree(d_src):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    gather_empty_d(d_working=d_src)
