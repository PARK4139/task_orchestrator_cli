def debug_call_depth(func_n):
    import inspect

    depth = len(inspect.stack(0))
    print(f"[DEBUG] CALL DEPTH ({func_n}): {depth}")
    return depth
