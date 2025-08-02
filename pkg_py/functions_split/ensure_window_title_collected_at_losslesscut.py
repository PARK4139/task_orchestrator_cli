from pkg_py.system_object.directories import D_PKG_HISTORY
from pkg_py.system_object.local_test_activate import LTA


def log_step(step_name: str, extra: str = ""):
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    ensure_printed(f"[STEP] {step_name} {extra} {'%%%FOO%%%' if LTA else ''}")


def log_state_change(state, prev_state):
    from pkg_py.functions_split.ensure_state_printed import ensure_state_printed
    if state != prev_state:
        ensure_state_printed(state=state, pk_id="[STATE]")
        return state.copy()
    return prev_state


def detect_losslesscut_window_titles():
    """LosslessCut 관련 윈도우 타이틀들을 감지하여 반환"""
    from pkg_py.functions_split.get_window_title_list import get_window_title_list

    all_titles = get_window_title_list()
    losslesscut_titles = []

    for title in all_titles:
        if "LosslessCut" in title:
            losslesscut_titles.append(title)

    return losslesscut_titles


def log_window_title_change(prev_titles, current_titles):
    """윈도우 타이틀 변화를 감지하고 출력"""
    from pkg_py.functions_split.ensure_printed import ensure_printed

    if prev_titles != current_titles:
        ensure_printed(f"[WINDOW_TITLE_CHANGE] Previous: {prev_titles}")
        ensure_printed(f"[WINDOW_TITLE_CHANGE] Current: {current_titles}")

        # 새로 나타난 타이틀들
        new_titles = [title for title in current_titles if title not in prev_titles]
        if new_titles:
            ensure_printed(f"[WINDOW_TITLE_CHANGE] New titles: {new_titles}")

        # 사라진 타이틀들
        removed_titles = [title for title in prev_titles if title not in current_titles]
        if removed_titles:
            ensure_printed(f"[WINDOW_TITLE_CHANGE] Removed titles: {removed_titles}")

        return True
    return False


def handle_state_event(event_type, state, f_video_to_load, **kwargs):
    """상태 이벤트를 처리하는 함수"""
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_pressed import ensure_pressed
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
    from pkg_py.functions_split.is_window_title_front import is_window_title_front
    from pkg_py.functions_split.ensure_video_playied_at_losslesscut import ensure_video_playied_at_losslesscut
    from pkg_py.functions_split.get_nx import get_nx

    ensure_printed(f"[EVENT] {event_type} triggered")

    if event_type == "LOSSESSCUT_STARTED":
        log_step("EVENT_LOSSESSCUT_STARTED", "LosslessCut application started")
        state['running'] = 1
        state['loading'] = 0
        state['loaded'] = 0
        state['playing'] = 0

    elif event_type == "VIDEO_LOADING_STARTED":
        log_step("EVENT_VIDEO_LOADING_STARTED", "Video loading started")
        state['loading'] = 1
        state['loaded'] = 0
        state['playing'] = 0

    elif event_type == "VIDEO_LOADED":
        log_step("EVENT_VIDEO_LOADED", f"Video loaded: {get_nx(f_video_to_load)}")
        state['loading'] = 0
        state['loaded'] = 1
        state['playing'] = 0

    elif event_type == "VIDEO_PLAY_STARTED":
        log_step("EVENT_VIDEO_PLAY_STARTED", "Video play started")
        state['playing'] = 1

    elif event_type == "VIDEO_PLAY_STOPPED":
        log_step("EVENT_VIDEO_PLAY_STOPPED", "Video play stopped")
        state['playing'] = 0

    elif event_type == "VIDEO_ENDED":
        log_step("EVENT_VIDEO_ENDED", "Video ended")
        state['running'] = 0
        state['loading'] = 0
        state['loaded'] = 0
        state['playing'] = 0

    elif event_type == "LOSSESSCUT_CLOSED":
        log_step("EVENT_LOSSESSCUT_CLOSED", "LosslessCut application closed")
        state['running'] = 0
        state['loading'] = 0
        state['loaded'] = 0
        state['playing'] = 0

    elif event_type == "ACTION_PLAY_VIDEO":
        log_step("EVENT_ACTION_PLAY_VIDEO", "Executing play video action")
        window_title = f"{get_nx(f_video_to_load)} - LosslessCut"
        ensure_window_to_front(window_title_seg=window_title)
        if is_window_title_front(window_title):
            ensure_video_playied_at_losslesscut()
            state['playing'] = 1

    elif event_type == "ACTION_PLAY_FULLSCREEN":
        log_step("EVENT_ACTION_PLAY_FULLSCREEN", "Executing fullscreen play action")
        window_title = f"{get_nx(f_video_to_load)} - LosslessCut"
        ensure_window_to_front(window_title_seg=window_title)
        if is_window_title_front(window_title):
            ensure_pressed("esc")
            ensure_slept(milliseconds=300)
            ensure_pressed("space")
            state['playing'] = 1
            ensure_slept(milliseconds=300)
            ensure_pressed("f11")
            ensure_slept(milliseconds=300)

    elif event_type == "ACTION_LOAD_VIDEO":
        log_step("EVENT_ACTION_LOAD_VIDEO", f"Loading video: {f_video_to_load}")
        from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
        ensure_f_video_loaded_on_losslesscut(f_video_to_load)
        state['loading'] = 1
        state['playing'] = 0

    elif event_type == "ACTION_RESTART_LOSSESSCUT":
        log_step("EVENT_ACTION_RESTART_LOSSESSCUT", "Restarting LosslessCut")
        from pkg_py.functions_split.ensure_losslesscut_ran import ensure_losslesscut_ran
        ensure_losslesscut_ran()
        state['running'] = 1
        state['loading'] = 0
        state['loaded'] = 0
        state['playing'] = 0
        ensure_slept(milliseconds=2000)

    return state


def ensure_video_played_at_losslesscut_v6(max_files=30):
    import time
    import traceback
    import inspect
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_list_calculated import get_list_calculated
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
    from pkg_py.functions_split.ensure_start_time_logged import ensure_start_time_logged
    from pkg_py.system_object.state_via_database import PkSqlite3DB
    from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
    from pkg_py.system_object.directories import D_DOWNLOADS, D_PK_WORKING
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.functions_split.get_list_sorted import get_list_sorted
    from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
    from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
    from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
    from pkg_py.functions_split.ensure_losslesscut_ran import ensure_losslesscut_ran
    from pkg_py.functions_split.get_historical_list import get_historical_list
    from pkg_py.functions_split.get_window_title_list import get_window_title_list
    from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
    from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
    import os

    start_time = ensure_start_time_logged()
    func_n = inspect.currentframe().f_code.co_name
    pk_db = PkSqlite3DB()

    INTERVAL_MAX = 5000
    INTERVAL_ORIGIN = 100
    INTERVAL_DELTA = 200

    # 수집 모드 플래그
    COLLECTION_MODE = True  # True: 수집 모드, False: 실행 모드


    # 로그 파일을 D_PKG_LOG에 저장
    from pkg_py.system_object.directories import D_PKG_LOG
    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
    window_title_logfile = os.path.join(D_PKG_LOG, "losslesscut_titles.log")
    window_title_logfile= get_pnx_os_style(window_title_logfile)
    ensure_pnx_made(window_title_logfile, mode="file")

    # 수집된 파일을 자동으로 열기
    ensure_pnx_opened_by_ext(window_title_logfile)
    
    # 중복 제거를 위한 set
    seen_titles = set()

    try:
        key_name = "d_working"
        file_to_working = rf"{D_PKG_HISTORY}/{get_file_id(key_name, func_n)}.history"
        file_to_working = get_pnx_os_style(file_to_working)
        historical_pnxs = get_historical_list(f=file_to_working)
        options = historical_pnxs + get_list_sorted(working_list=[D_PK_WORKING, D_DOWNLOADS], mode_asc=1)
        if LTA:
            d_working = rf"G:\Downloads\pk_working"
        else:
            d_working = get_value_completed(key_hint='d_working=', values=options)

        d_working = get_pnx_os_style(pnx=d_working).strip()

        ensure_printed(f"[DATA] len(historical_pnxs)={len(historical_pnxs)}")
        ensure_printed(f"[DATA] len(options)={len(options)}")

        values_to_save = [v for v in [d_working] + historical_pnxs + options if does_pnx_exist(pnx=v)]
        values_to_save = get_list_calculated(origin_list=values_to_save, dedup=True)
        ensure_list_written_to_f(f=file_to_working, working_list=values_to_save, mode="w")

        ext_allowed_list = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm']
        video_ignored_keyword_list = ['-seg', 'SEG-']

        loop_cnt = 1
        f_video_to_load = None
        f_videos_allowed = []

        ensure_losslesscut_ran()

        while True:
            ensure_console_cleared()

            # 윈도우 타이틀 수집 (항상 실행)
            window_titles = get_window_title_list()
            losslesscut_titles = [title for title in window_titles if "LosslessCut" in title]

            # 수집 모드일 때는 타이틀만 수집하고 다른 로직은 주석처리
            if COLLECTION_MODE:
                new_titles = []
                for title in losslesscut_titles:
                    if title not in seen_titles:
                        new_titles.append(title)
                        seen_titles.add(title)
                
                if new_titles:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    for title in new_titles:
                        log_data = f"[{timestamp}] {title}\n"
                        with open(window_title_logfile, "a", encoding="utf-8") as f:
                            f.write(log_data)
                    ensure_printed(f"[COLLECT] {len(new_titles)} new titles logged to {window_title_logfile}")
                else:
                    ensure_printed(f"[COLLECT] No new titles found (total seen: {len(seen_titles)})")
                
                time.sleep(1)
                continue

            # 2. 상태 분기: 편집/출력/로딩/재생 등 (루프 내 직접)
            current_state = "idle"
            for title in losslesscut_titles:  # Use losslesscut_titles here
                if "출력" in title or "Export" in title:
                    current_state = "exporting"
                    break
                if "편집" in title or "Edit" in title:
                    current_state = "editing"
                    break
                if "불러오는 중" in title or "Loading" in title:
                    current_state = "loading"
                    break
                if any(ext in title for ext in [".mp4", ".mkv", ".avi"]):
                    current_state = "playing"
                    break
            ensure_printed(f"[STATE] {current_state}")


            # 3. 편집/출력 중에는 자동 로드/재생 금지
            if current_state in ("editing", "exporting"):
                ensure_printed("[INFO] 편집/출력 중이므로 자동 로드/재생을 건너뜀")
                time.sleep(2)
                continue

            # 4. 비디오 자동 로드/재생 (idle, loading, playing만 허용)
            if f_video_to_load is None:
                f_videos_allowed = get_video_filtered_list(d_working, ext_allowed_list, video_ignored_keyword_list)[:max_files]
                f_video_to_load = get_f_video_to_load(f_videos_allowed)
                ensure_printed(f"[INFO] 로드할 비디오: {f_video_to_load}")

            if current_state == "idle":
                ensure_printed("[INFO] LosslessCut이 대기 상태, 비디오 자동 로드")
                ensure_f_video_loaded_on_losslesscut(f_video_to_load)
                time.sleep(1)
                continue

            if current_state == "playing":
                ensure_printed("[INFO] 비디오가 이미 재생 중입니다.")
                # 필요시 자동 재생 트리거 추가
                # ensure_video_playied_at_losslesscut()
                time.sleep(2)
                continue

            if current_state == "loading":
                ensure_printed("[INFO] 비디오 로딩 중입니다.")
                time.sleep(2)
                continue

            # 기타 상태(예: LosslessCut이 꺼져있음 등)
            time.sleep(2)
            loop_cnt += 1

    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
