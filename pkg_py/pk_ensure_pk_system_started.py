if __name__ == '__main__':
    from pkg_py.functions_split.colorama_init_once import colorama_init_once
    from pkg_py.functions_split.ensure_pk_system_started import ensure_pk_system_started

    try:
        colorama_init_once()
        ensure_pk_system_started()
    except:
        import traceback

        traceback.print_exc()
