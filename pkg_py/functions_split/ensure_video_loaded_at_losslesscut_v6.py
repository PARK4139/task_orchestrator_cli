from pkg_py.system_object.directories import D_PKG_TXT


def log_step(step_name: str, extra: str = ""):
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    ensure_printed(f"[STEP] {step_name} {extra} {'%%%FOO%%%' if LTA else ''}")


def log_state_change(state, prev_state):
    from pkg_py.functions_split.ensure_state_printed import ensure_state_printed
    if state != prev_state:
        ensure_state_printed(state=state, pk_id="[STATE_CHANGE]")


def analyze_losslesscut_state(window_title):
    """LosslessCut 윈도우 타이틀을 분석하여 상태를 반환"""
    if "Exporting" in window_title:
        return "EXPORTING"  # 출력 중 - 로드/재생 금지
    elif " - " in window_title and not "Exporting" in window_title:
        return "FILE_LOADED"  # 파일 로드됨 - 재생 가능
    elif window_title == "LosslessCut":
        return "IDLE"  # 기본 상태 - 파일 로드 가능
    else:
        return "UNKNOWN"


def wait_for_mouse_click():
    """마우스 클릭을 기다리는 함수 (win32api 사용)"""
    import win32api
    import win32con
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_current_mouse_abs_info import get_current_mouse_abs_info
    import time

    ensure_printed("[WAIT] 마우스 클릭을 기다리는 중...")

    # 마우스 클릭 감지
    while True:
        # 왼쪽 마우스 버튼이 눌렸는지 확인
        if win32api.GetAsyncKeyState(win32con.VK_LBUTTON) & 0x8000:
            # 클릭이 감지되면 현재 마우스 위치 반환
            x, y = get_current_mouse_abs_info()
            ensure_printed(f"[CLICK] 마우스 클릭 감지됨: ({x}, {y})")
            return int(x), int(y)

        # CPU 사용량을 줄이기 위해 짧은 대기
        time.sleep(0.01)


def learn_coordinates_by_mouse(coords_file):
    """Close 버튼의 좌표를 학습하여 파일에 저장"""
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made

    # 좌표 파일 경로
    ensure_printed("[LEARN] Close 버튼 좌표 학습을 시작합니다.")
    ensure_printed("[LEARN] 1. LosslessCut export dialog가 보이는 상태에서")
    ensure_printed("[LEARN] 2. Close 버튼을 클릭해주세요.")
    ensure_printed("[LEARN] 3. 클릭한 위치의 좌표가 자동으로 저장됩니다.")

    # 마우스 클릭 대기
    x, y = wait_for_mouse_click()

    # 좌표를 파일에 저장
    ensure_pnx_made(coords_file, mode="file")
    with open(coords_file, 'w') as f:
        f.write(f"{x},{y}")

    ensure_printed(f"[LEARN] Close 버튼 좌표가 저장되었습니다: ({x}, {y})")
    ensure_printed(f"[LEARN] 저장 위치: {coords_file}")

    return x, y


def get_coords_leared_by_mouse(coords_file):
    """Close 버튼의 좌표를 캐시에서 가져오거나 새로 학습하여 반환"""
    from pkg_py.functions_split.ensure_printed import ensure_printed
    import os

    # 캐시 파일 경로
    coords_file = coords_file

    # 캐시에서 좌표 확인
    if os.path.exists(coords_file):
        try:
            with open(coords_file, 'r') as f:
                cached_coords = f.read().strip()
                if cached_coords:
                    x, y = map(int, cached_coords.split(','))
                    ensure_printed(f"[CACHE] 캐시된 Close 버튼 좌표 사용: ({x}, {y})")
                    return x, y
        except Exception as e:
            ensure_printed(f"[ERROR] 캐시 파일 읽기 실패: {e}")

    # 캐시가 없으면 새로 학습
    ensure_printed("[LEARN] 캐시된 좌표가 없습니다. 새로 학습합니다.")
    return learn_coordinates_by_mouse(coords_file)


def ensure_coords_clicked(coords_file):
    """Close 버튼 클릭 (학습된 좌표 사용)"""
    from pkg_py.functions_split.click_mouse_left_btn import click_mouse_left_btn
    from pkg_py.functions_split.ensure_printed import ensure_printed

    # 학습된 좌표 가져오기
    coords_leared = get_coords_leared_by_mouse(coords_file)

    if coords_leared:
        x, y = coords_leared
        click_mouse_left_btn(x_abs=x, y_abs=y)
        ensure_printed(f"[CLICK] Close 버튼 클릭: ({x}, {y})")
        return True
    else:
        ensure_printed("[ERROR] Close 버튼 좌표를 찾을 수 없습니다.")
        return False


def ensure_video_loaded_at_losslesscut_v6(max_files=30):
    import time
    from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
    import traceback
    from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
    from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
    from pkg_py.functions_split.ensure_losslesscut_ran import ensure_losslesscut_ran
    from pkg_py.functions_split.get_historical_list import get_historical_list
    from pkg_py.functions_split.get_list_sorted import get_list_sorted
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.system_object.directories import D_PKG_HISTORY, D_DOWNLOADS, D_PK_WORKING
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025

    import inspect
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_list_calculated import get_list_calculated
    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_window_title_list import get_window_title_list
    from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
    from pkg_py.functions_split.ensure_video_playied_at_losslesscut import ensure_video_playied_at_losslesscut
    from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
    from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.system_object.directories import D_PKG_LOG
    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
    from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
    import os

    func_n = inspect.currentframe().f_code.co_name

    # 수집 모드 플래그 (False로 변경하여 자동화 모드 활성화)
    COLLECTION_MODE = False
    window_title_logfile = os.path.join(D_PKG_LOG, "losslesscut_titles.log")
    ensure_pnx_made(window_title_logfile, mode="file")
    if COLLECTION_MODE:
        ensure_pnx_opened_by_ext(window_title_logfile)

    # 중복 제거를 위한 set
    seen_titles = set()

    # 상태 추적 변수들
    current_state = "UNKNOWN"
    prev_state = None
    export_completed = False
    last_export_time = None
    file_loaded_after_export = False

    # 재생 상태 추적 변수 추가
    play_attempted = False  # 현재 파일에 대해 재생 시도 여부
    current_file_loaded = None  # 현재 로드된 파일명 추적

    # 비디오 파일 목록 가져오기 (v5 방식 사용)
    ext_allowed_list = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm']
    video_ignored_keyword_list = ['-seg', 'SEG-']

    # 정규표현식 패턴 추가 - 시간 범위 패턴 제외
    video_ignored_regex_patterns = [
        r'\d{2}\.\d{2}\.\d{2}\.\d{3}-\d{2}\.\d{2}\.\d{2}\.\d{3}',  # 00.00.58.565-00.46.21.342 패턴
        r'\d{2}\.\d{2}\.\d{2}-\d{2}\.\d{2}\.\d{2}',  # 00.00.58-00.46.21 패턴 (밀리초 없는 버전)
    ]

    key_name = "d_working"
    file_to_working = rf"{D_PKG_HISTORY}/{get_file_id(key_name, func_n)}.history"
    file_to_working = get_pnx_os_style(file_to_working)
    historical_pnxs = get_historical_list(f=file_to_working)
    options = historical_pnxs + get_list_sorted(working_list=[D_PK_WORKING, D_DOWNLOADS], mode_asc=1)
    if LTA:
        # d_working = rf"G:\Downloads\pk_working"
        d_working = rf"G:\Downloads\pk_working\pk_working_s"
    else:
        d_working = get_value_completed(key_hint='d_working=', values=options)
    d_working = get_pnx_os_style(pnx=d_working).strip()
    ensure_printed(f'''[{PkMessages2025.DATA}] len(historical_pnxs)={len(historical_pnxs)} {'%%%FOO%%%' if LTA else ''}''')
    ensure_printed(f'''[{PkMessages2025.DATA}] len(options)={len(options)} {'%%%FOO%%%' if LTA else ''}''')
    values_to_save = [v for v in [d_working] + historical_pnxs + options if does_pnx_exist(pnx=v)]
    values_to_save = get_list_calculated(origin_list=values_to_save, dedup=True)
    ensure_list_written_to_f(f=file_to_working, working_list=values_to_save, mode="w")
    f_videos_allowed = get_video_filtered_list(d_working, ext_allowed_list, video_ignored_keyword_list, video_ignored_regex_patterns)[:max_files]
    f_video_to_load = get_f_video_to_load(f_videos_allowed)

    current_video_index = 0

    # LosslessCut 재시작 추적 변수 추가
    losslesscut_restart_attempted = False

    try:
        # 비디오 파일 목록 가져오기 (기존 로직 사용)
        from pkg_py.functions_split.get_list_calculated import get_list_calculated
        from pkg_py.system_object.directories import D_DOWNLOADS

        # 비디오 파일 확장자
        video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm']

        # 다운로드 폴더에서 비디오 파일 찾기
        video_files = []
        if os.path.exists(D_DOWNLOADS):
            for file in os.listdir(D_DOWNLOADS):
                if any(file.lower().endswith(ext) for ext in video_extensions):
                    video_files.append(os.path.join(D_DOWNLOADS, file))

        # 최대 파일 수 제한
        video_files = video_files[:max_files]

        # v5에서 사용한 함수들 추가
        from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
        from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load

        # 비디오 파일 목록 가져오기 (v5 방식 사용)
        ext_allowed_list = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm']
        video_ignored_keyword_list = ['-seg', 'SEG-']
        f_videos_allowed = get_video_filtered_list(D_DOWNLOADS, ext_allowed_list, video_ignored_keyword_list)[:max_files]

        current_video_index = 0

        loop_cnt = 1

        ensure_losslesscut_ran()

        coords_file = os.path.join(D_PKG_TXT, "losslesscut_close_coordinates.txt")
        editable = True  # pk_option
        # editable=False # pk_option
        if editable:
            ensure_printed("[EDIT] 좌표 파일을 열어서 수정할 수 있습니다.")
            ensure_pnx_opened_by_ext(coords_file)
        while True:
            # ensure_console_cleared()

            # LosslessCut 실행 상태 확인 (항상 먼저 체크)
            if not is_losslesscut_running():
                if not losslesscut_restart_attempted:
                    log_step("AUTO_LOSSLESSCUT_NOT_RUNNING", "LosslessCut 실행되지 않음 - 재시작")
                    ensure_losslesscut_ran()
                    losslesscut_restart_attempted = True
                    # 재시작 후 잠시 대기
                    time.sleep(3)
                else:
                    log_step("AUTO_LOSSLESSCUT_RESTART_WAITING", "LosslessCut 재시작 대기 중...")
                    time.sleep(2)
                continue  # LosslessCut이 실행되지 않으면 다른 로직 건너뛰기

            # LosslessCut이 실행되면 재시작 플래그 초기화
            losslesscut_restart_attempted = False

            # 윈도우 타이틀 수집
            window_titles = get_window_title_list()
            losslesscut_titles = [title for title in window_titles if "LosslessCut" in title]

            # 수집 모드일 때는 타이틀만 수집
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
                    ensure_printed(f"[COLLECT] {len(new_titles)} new titles logged")

                time.sleep(1)
                continue

            # f_video_to_load가 None이면 다음 파일 선택
            if f_video_to_load is None:
                f_video_to_load = get_f_video_to_load(f_videos_allowed)
                if f_video_to_load is None:
                    log_step("AUTO_NO_MORE_FILES", "더 이상 로드할 파일이 없음")
                    continue
                log_step("AUTO_FILE_SELECTED", f"선택된 파일: {get_nx(f_video_to_load)}")
                play_attempted = False  # 새 파일이면 재생 시도 플래그 초기화
                current_file_loaded = None  # 현재 로드된 파일명 초기화

            # 자동화 모드 - 상태 분석 및 자동화 실행
            if losslesscut_titles:
                current_title = losslesscut_titles[0]
                current_state = analyze_losslesscut_state(current_title)

                # 상태 변화 로깅
                if current_state != prev_state:
                    log_step("STATE_CHANGE", f"{prev_state} → {current_state}")
                    log_state_change(current_state, prev_state)

                # 상태별 자동화 로직
                if current_state == "EXPORTING":
                    log_step("AUTO_EXPORTING", "출력 중 - 대기")
                    export_completed = False
                    last_export_time = time.time()

                elif current_state == "IDLE" and prev_state == "EXPORTING":
                    # 출력 완료 후 IDLE 상태로 돌아옴
                    log_step("AUTO_EXPORT_COMPLETED", "출력 완료 - 다음 파일 로드 준비")
                    export_completed = True
                    file_loaded_after_export = False
                    # 비디오 목록 다시 로드
                    f_videos_allowed = get_video_filtered_list(d_working, ext_allowed_list, video_ignored_keyword_list)[:max_files]
                    # 다음 파일 선택 및 바로 로드
                    f_video_to_load = get_f_video_to_load(f_videos_allowed)
                    if f_video_to_load is not None:
                        log_step("AUTO_NEXT_FILE_SELECTED", f"다음 파일 선택: {get_nx(f_video_to_load)}")
                        ensure_f_video_loaded_on_losslesscut(f_video_to_load)
                        play_attempted = False
                        current_file_loaded = None
                    else:
                        log_step("AUTO_NO_MORE_FILES", "더 이상 로드할 파일이 없음")

                elif current_state == "FILE_LOADED":
                    # 현재 로드된 파일명 추출
                    loaded_filename = None
                    if " - " in current_title:
                        loaded_filename = current_title.split(" - ")[1].replace(" - LosslessCut", "")

                    # 새 파일이 로드되었는지 확인
                    if loaded_filename != current_file_loaded:
                        current_file_loaded = loaded_filename
                        play_attempted = False  # 새 파일이면 재생 시도 플래그 초기화
                        log_step("AUTO_NEW_FILE_DETECTED", f"새 파일 감지: {loaded_filename}")

                    if export_completed and not file_loaded_after_export:
                        # 출력 완료 후 새 파일이 로드됨
                        log_step("AUTO_FILE_LOADED_AFTER_EXPORT", "새 파일 로드됨 - 재생 시도")
                        file_loaded_after_export = True
                        if not play_attempted:
                            ensure_video_playied_at_losslesscut()
                            play_attempted = True
                            log_step("AUTO_PLAY_ATTEMPTED", "재생 시도 완료")
                            # 재생 후 Close 버튼 클릭
                            time.sleep(2)  # 재생 시작 대기
                            ensure_coords_clicked(coords_file=coords_file)
                    elif not export_completed:
                        # 일반적인 파일 로드
                        log_step("AUTO_FILE_LOADED", "파일 로드됨 - 재생 시도")
                        if not play_attempted:
                            ensure_video_playied_at_losslesscut()
                            play_attempted = True
                            log_step("AUTO_PLAY_ATTEMPTED", "재생 시도 완료")
                            # 재생 후 Close 버튼 클릭
                            time.sleep(2)  # 재생 시작 대기
                            ensure_coords_clicked(coords_file=coords_file)

                elif current_state == "IDLE" and not export_completed:
                    # 일반적인 IDLE 상태 - 파일 로드 시도
                    # f_video_to_load가 None이면 다음 파일 선택
                    if f_video_to_load is None:
                        f_video_to_load = get_f_video_to_load(f_videos_allowed)
                        if f_video_to_load is None:
                            log_step("AUTO_NO_MORE_FILES", "더 이상 로드할 파일이 없음")
                            continue
                        log_step("AUTO_FILE_SELECTED", f"선택된 파일: {get_nx(f_video_to_load)}")
                        play_attempted = False
                        current_file_loaded = None

                    log_step("AUTO_IDLE", f"IDLE 상태 - 파일 로드 시도: {get_nx(f_video_to_load)}")
                    ensure_f_video_loaded_on_losslesscut(f_video_to_load)

                prev_state = current_state
            else:
                # LosslessCut이 실행 중이지만 타이틀이 없는 경우 (초기 로딩 중)
                log_step("AUTO_LOSSLESSCUT_LOADING", "LosslessCut 초기 로딩 중...")

            time.sleep(1)

    except Exception as e:
        ensure_do_exception_routine(traceback=traceback, exception=e)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
