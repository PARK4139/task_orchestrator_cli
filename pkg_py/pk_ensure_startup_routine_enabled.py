if __name__ == "__main__":
    from pkg_py.functions_split.ensure_pk_system_started import ensure_pk_system_started
    from pkg_py.functions_split.ensure_chatgpt_opened import ensure_chatgpt_opened
    from pkg_py.functions_split.ensure_vscode_enabled import ensure_vscode_enabled
    import traceback
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.ensure_cursor_enabled import ensure_cursor_enabled
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.functions_split.ensure_memo_editable import ensure_memo_editable
    from pkg_py.functions_split.ensure_pycharm_opened import ensure_pycharm_opened
    from pkg_py.functions_split.ensure_sound_track_played import ensure_sound_track_played
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.system_object.directories  import D_PROJECT

    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        ensure_sound_track_played()  # work with music

        ensure_memo_editable()
        ensure_pycharm_opened()
        ensure_cursor_enabled()
        ensure_vscode_enabled()
        ensure_chatgpt_opened()

        # TODO pk_system 을 백그라운드에서  단축키를 탐지하여 열도록 수정.
        # TODO pk_system process monitor and controlrer  # windows 타이틀 수집해서    pk_ensure_  패턴이 있는것들을 수집.

        ensure_pk_system_started(loop_mode=False)  # pk_option

        # ensure_program_suicided(__file__)  # pk_option
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
