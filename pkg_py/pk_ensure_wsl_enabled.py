from pkg_py.functions_split.assist_to_control_wsl import assist_to_control_wsl
from pkg_py.functions_split.debug_state_for_py_data_type import debug_state_for_py_data_type
from pkg_py.functions_split.ensure_printed import ensure_printed

if __name__ == "__main__":
    import traceback
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    import sys
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))


        state_wsl_enabled, wsl_cmd_map_dict = ensure_wsl_enabled()
        if not state_wsl_enabled:
            debug_state_for_py_data_type(pk_stamp='%%%FOO%%%-2', data_working=wsl_cmd_map_dict)
            ensure_printed("wsl installed", print_color='red')
            sys.exit(0)
        else:
            if LTA:
                debug_state_for_py_data_type(pk_stamp='%%%FOO%%%-3', data_working=wsl_cmd_map_dict)
                ensure_printed("wsl installed", print_color='green')

        wsl_cmd_list = list(wsl_cmd_map_dict.keys())
        pk_config_dict = {
            'pk_wsl_controller_version': 'pk_wsl_version.2.0.0',
            'pk_wsl_cmd_exec_map_dict': wsl_cmd_map_dict,
            'pk_wsl_cmd_list': wsl_cmd_list,
            'pk_wsl_cmd_list_len': len(wsl_cmd_list),
            'pk_wsl_cmd_map_dict': {idx: cmd for idx, cmd in enumerate(wsl_cmd_list)}
        }
        assist_to_control_wsl(**pk_config_dict)
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
