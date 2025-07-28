if __name__ == '__main__':
    from pkg_py.functions_split.ensure_process_killed import ensure_process_killed
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    import traceback
    from pkg_py.functions_split.get_nx import get_nx

    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.ensure_pk_system_started import ensure_pk_system_started

    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        ensure_pk_system_started()

        ensure_process_killed(window_title=get_nx(__file__))  # pk_option

    except:

        traceback.print_exc()
