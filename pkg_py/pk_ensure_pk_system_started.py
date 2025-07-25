if __name__ == '__main__':
    from pkg_py.functions_split.pk_colorama_init_once import pk_colorama_init_once
    from pkg_py.functions_split.ensure_pk_system_started import pk_ensure_pk_system_started

    try:
        pk_colorama_init_once()
        pk_ensure_pk_system_started()
    except:
        import traceback

        traceback.print_exc()
