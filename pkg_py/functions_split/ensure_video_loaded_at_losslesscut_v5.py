def ensure_video_loaded_at_losslesscut_v5(max_files=30):
    from pkg_py.functions_split.ensure_console_paused import ensure_console_paused
    from pkg_py.functions_split.ensure_text_divider_printed import ensure_text_divider_printed
    from pkg_py.functions_split.ensure_video_playied_at_losslesscut import ensure_video_playied_at_losslesscut

    import traceback
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_list_calculated import get_list_calculated

    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

    from pkg_py.functions_split.ensure_start_time_logged import ensure_start_time_logged
    from pkg_py.system_object.map_massages import PkMessages2025

    from pkg_py.functions_split.ensure_interval_based_on_state_updated import ensure_interval_based_on_state_updated
    from pkg_py.functions_split.get_current_interval import get_current_interval
    from pkg_py.functions_split.get_db_id import get_db_id
    from pkg_py.system_object.state_via_database import PkSqlite3DB

    from pkg_py.functions_split.ensure_pressed import ensure_pressed
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.functions_split.ensure_state_printed import ensure_state_printed

    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
    from pkg_py.system_object.directories import D_PK_WORKING
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared

    from pkg_py.functions_split.get_list_sorted import get_list_sorted
    from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_value_completed import get_value_completed

    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
    from pkg_py.functions_split.is_window_opened import is_window_opened
    from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
    from pkg_py.functions_split.is_window_title_front import is_window_title_front
    from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
    from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
    from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
    from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
    from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
    from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
    from pkg_py.functions_split.get_historical_list import get_historical_list

    import inspect

    start_time = ensure_start_time_logged()
    func_n = inspect.currentframe().f_code.co_name
    F_CACHE = f"{D_PKG_PKL}/{func_n}.pkl"
    pk_db = PkSqlite3DB()

    INTERVAL_MAX = 5000
    INTERVAL_ORIGIN = 100
    INTERVAL_DELTA = 200

    try:
        key_name = "d_working"
        file_to_working = get_file_id(key_name, func_n)
        historical_pnxs = get_historical_list(f=file_to_working)
        options = historical_pnxs + get_list_sorted(working_list=[D_PK_WORKING, D_DOWNLOADS], mode_asc=1)
        d_working = get_value_completed(key_hint='d_working=', values=options)
        ensure_printed(f'''[{PkMessages2025.DATA}] len(historical_pnxs)={len(historical_pnxs)} {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''[{PkMessages2025.DATA}] len(options)={len(options)} {'%%%FOO%%%' if LTA else ''}''')
        d_working = get_pnx_os_style(pnx=d_working).strip()
        values_to_save = [v for v in [d_working] + historical_pnxs + options if does_pnx_exist(pnx=v)]
        values_to_save = get_list_calculated(origin_list=values_to_save, dedup=True)
        ensure_list_written_to_f(f=file_to_working, working_list=values_to_save, mode="w")

        ext_allowed_list = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm']
        video_ignored_keyword_list = ['-seg', 'SEG-']
        f_video_to_load = None
        f_videos_allowed = None
        loop_cnt = 1
        state = {'running': 0, 'loading': 0, 'loaded': 0, 'playing': 0}
        prev_state = None

        while True:
            ensure_text_divider_printed()  # pk_option
            ensure_console_paused()
            ensure_console_cleared()  # pk_option

            if f_video_to_load is None:
                ensure_printed(f'''f_video_to_load is None {'%%%FOO%%%' if LTA else ''}''')
                f_videos_allowed = get_video_filtered_list(d_working, ext_allowed_list, video_ignored_keyword_list)[:max_files]
                f_video_to_load = get_f_video_to_load(f_videos_allowed)
                continue

            if state != prev_state:
                ensure_state_printed(state=state, pk_id="%%%FOO%%%")
                prev_state = state.copy()

            if not does_pnx_exist(pnx=f_video_to_load):
                f_video_to_load = get_f_video_to_load(f_videos_allowed)
                pk_db.set_values(values=[str(INTERVAL_ORIGIN)], db_id=get_db_id(key_name="speed_control_interval_ms", func_n=func_n))
                state['playing'] = 0

            if state == {'running': 1, 'loading': 1, 'loaded': 1, 'playing': 0}:
                if is_window_opened("정리 중 - LosslessCut"):
                    state = {'running': 0, 'loading': 0, 'loaded': 0, 'playing': 0}
                    continue

            if not is_losslesscut_running():
                ensure_losslesscut_reran()
                state['running'] = 1
                ensure_f_video_loaded_on_losslesscut(f_video_to_load)
                state['playing'] = 0
            else:
                state['running'] = 1

            if is_window_title_opened("LosslessCut"):
                ensure_f_video_loaded_on_losslesscut(f_video_to_load)
                state['playing'] = 0
                continue

            for loading_title in [
                "Loading file - LosslessCut",
                "파일 불러오는 중 - LosslessCut",
                f"파일 불러오는 중 - {get_nx(f_video_to_load)} - LosslessCut"
            ]:
                if is_window_title_opened(loading_title):
                    ensure_window_to_front(window_title_seg=loading_title)
                    if is_window_title_front(loading_title):
                        ensure_pressed("esc")
                    state['loading'] = 1
                    state['playing'] = 0
                    break

            if is_window_title_opened(f"{get_nx(f_video_to_load)} - LosslessCut"):
                state['loaded'] = 1

            if state == {'running': 1, 'loading': 1, 'loaded': 1, 'playing': 0}:
                window_title = f"{get_nx(f_video_to_load)} - LosslessCut"
                while True:
                    ensure_window_to_front(window_title_seg=window_title)
                    if is_window_title_front(window_title):
                        ensure_video_playied_at_losslesscut()
                        state['playing'] = 1
                        ensure_printed(f'''step 1{'%%%FOO%%%' if LTA else ''}''')
                        break

            if state == {'running': 1, 'loading': 0, 'loaded': 1, 'playing': 0}:
                window_title = f"{get_nx(f_video_to_load)} - LosslessCut"
                while True:
                    ensure_window_to_front(window_title_seg=window_title)
                    if is_window_title_front(window_title):
                        ensure_pressed("esc")
                        ensure_slept(milliseconds=300)
                        ensure_pressed("space")
                        state['playing'] = 1
                        ensure_slept(milliseconds=300)
                        ensure_pressed("f11")
                        ensure_slept(milliseconds=300)
                        ensure_printed(f'''step 2{'%%%FOO%%%' if LTA else ''}''')
                        break
                state = {'running': 1, 'loading': 1, 'loaded': 1, 'playing': 1}

            ensure_interval_based_on_state_updated(pk_db=pk_db, state_current=state, func_n=func_n, INTERVAL_ORIGIN=INTERVAL_ORIGIN, INTERVAL_DELTA=INTERVAL_DELTA, INTERVAL_MAX=INTERVAL_MAX)
            ensure_slept(milliseconds=get_current_interval(pk_db=pk_db, func_n=func_n, INTERVAL_ORIGIN=INTERVAL_ORIGIN))
            loop_cnt += 1
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
