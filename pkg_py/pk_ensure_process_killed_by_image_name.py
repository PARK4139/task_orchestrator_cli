from pkg_py.functions_split.ensure_process_killed_by_image_name import ensure_process_killed_by_image_name

if __name__ == "__main__":
    import traceback

    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done

    from pkg_py.functions_split.ensure_tasklist_got import get_image_names_from_tasklist
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
    from pkg_py.system_object.directories  import D_PROJECT
    # pk_#
    import os

    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        file_name = os.path.basename(__file__)
        func_n = file_name.replace('.py', '')

        key_name = "img_name"
        img_name = get_values_from_historical_file_routine(
            file_id=get_file_id(key_name, func_n),
            key_hint=f'{key_name}=',
            options_default=get_image_names_from_tasklist(),
            editable=True
        )
        ensure_process_killed_by_image_name(img_name)
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
