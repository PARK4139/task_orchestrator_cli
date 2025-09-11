import logging
import threading
import traceback
from pathlib import Path
from typing import List
from typing import Optional, Tuple

from functions import ensure_slept
from functions.ensure_console_paused import ensure_console_paused
from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
from functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


class PkVideoPlayer:
    _instance = None
    _initialized = False
    _lock = threading.Lock()  # (권장) 멀티스레드 안전

    def __new__(cls, *args, **kwargs):

        # 인자(f_video_player 포함)는 __new__에 먼저 들어오므로, 시그니처는 *args, **kwargs로 받는 게 안전
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, f_video_player, d_working: Path = None):
        import logging
        from pathlib import Path
        from typing import List, Set, Dict, Any
        from typing import Optional

        self.f_video_player = f_video_player
        self.window_title_next = None
        if PkVideoPlayer._initialized:
            return

        # ===== 경로 관련 속성 (Path 객체로 관리) =====
        self.d_working: Optional[Path] = d_working
        self.f_video_to_load: Optional[Path] = None
        self.f_videos_allowed: List[Path] = []

        # ===== 기본 설정 =====
        self.initialized: bool = False

        # ===== 상태 관리 =====
        self.current_state: str = "not_initialized"
        self.prev_state: Optional[str] = None
        self.play_attempted: bool = False
        self.export_detected: bool = False
        self.reload_needed: bool = False
        self.played_windows: Set[str] = set()

        # ===== 창 제목 분석 결과 =====
        self.current_window_title: Optional[str] = None
        self.extracted_filename: Optional[str] = None
        self.window_title_analysis_time: Optional[float] = None

        # ===== 상태별 창 이름 저장 =====
        self.window_titles_by_state: Dict[str, List[str]] = {
            "IDLE": [],
            "FILE_LOADED": [],
            "EXPORTING": [],
            "LOADING": [],
            "UNKNOWN": []
        }
        self.state_change_history: List[Dict[str, Any]] = []

        # ===== 재생 상태 세밀 관리 =====
        self.current_video_loaded: bool = False
        self.current_video_played: bool = False
        self.played_window: bool = False
        self.current_video_play_time: Optional[float] = None
        self.play_retry_count: int = 0
        self.max_play_retries: int = 3
        self.play_cooldown_seconds: int = 5

        # ===== 설정값들 =====
        # self.ext_allowed_list: List[str] = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm' ]
        self.ext_allowed_list: List[str] = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mp3', '.flac']

        # task_orchestrator_cli_option
        # self.video_name_parts_to_ignore: List[str] = []
        # self.video_ignored_regex_patterns: List[str] = []

        # task_orchestrator_cli_option
        self.video_name_parts_to_ignore: List[str] = ['-seg', 'SEG-']
        self.video_ignored_regex_patterns: List[str] = [
            r'\d{2}\.\d{2}\.\d{2}\.\d{3}-\d{2}\.\d{2}\.\d{2}\.\d{3}',
            r'\d{2}\.\d{2}\.\d{2}-\d{2}\.\d{2}\.\d{2}',
        ]

        # init video_player
        self.initialize_video_player()

        PkVideoPlayer._initialized = True
        logging.debug("[SINGLETON] LosslessCutState 인스턴스 초기화 완료")

    def initialize_video_player(self):
        import logging

        from sources.objects.pk_local_test_activate import LTA

        if self.d_working is None:
            if LTA:
                # task_orchestrator_cli_option
                self.d_working = self.get_d_working_from_routine()
                # self.d_working = str(D_DOWNLOADED_FROM_TORRENT)
                # self.d_working = str(D_PK_WORKING_S)
                # self.d_working = rf"F:\pk_archived\pk_sound\4"
            else:
                self.d_working = self.get_d_working_from_routine()

        if self.d_working and self.initialized:
            logging.debug(f"작업 디렉토리 이미 초기화됨: {self.d_working}")
            return

        logging.debug(f"작업 디렉토리 설정: {self.d_working}")

        self.update_video_to_load(self.d_working)

        if self.f_video_to_load:
            logging.debug(f"초기 비디오 파일 설정됨: {self.f_video_to_load.name}")
        else:
            logging.debug("초기 비디오 파일을 찾을 수 없음")

        self.initialized = True
        logging.debug(f"작업 디렉토리 초기화 완료: {self.d_working}")

        self.is_video_playing = False

    @property
    def current_file(self) -> Optional[Path]:

        return self.f_video_to_load

    @current_file.setter
    def current_file(self, value: Optional[Path]):

        self.f_video_to_load = value

    def update_video_to_load(self, d_working=None):
        import logging
        from pathlib import Path

        from sources.objects.pk_local_test_activate import LTA

        from sources.functions.get_video_filtered_list import get_video_filtered_list
        from sources.functions.get_f_video_to_load import get_f_video_to_load

        previous_video = self.f_video_to_load

        d_working = d_working or self.d_working

        logging.debug(rf"d_working={d_working}")
        logging.debug(rf"self.ext_allowed_list={self.ext_allowed_list}")
        logging.debug(rf"self.video_name_parts_to_ignore={self.video_name_parts_to_ignore}")
        logging.debug(rf"self.video_ignored_regex_patterns={self.video_ignored_regex_patterns}")

        logging.debug(rf"previous_video={previous_video}")
        videos = get_video_filtered_list(
            str(d_working), self.ext_allowed_list, self.video_name_parts_to_ignore, self.video_ignored_regex_patterns
        )
        logging.debug(rf"len(videos)={len(videos)}")
        self.f_videos_allowed = [Path(p) for p in videos]
        logging.debug(rf"self.f_videos_allowed={self.f_videos_allowed}")

        new_video = get_f_video_to_load([str(p) for p in self.f_videos_allowed])
        new_video = Path(new_video) if new_video else None
        logging.debug(f'''new_video={new_video} {'%%%FOO%%%' if LTA else ''}''')

        if new_video != previous_video:
            self.f_video_to_load = new_video
            self.reset_play_state()
            if self.f_video_to_load:
                logging.debug(f"새 파일 선택됨: {self.f_video_to_load.name}")
                logging.debug(f"재생 상태 초기화됨")
            else:
                logging.debug(f"로드할 파일이 없음")
        else:
            if self.f_video_to_load:
                logging.debug(f"같은 파일 유지: {self.f_video_to_load.name}")
            else:
                logging.debug(f"같은 파일 유지: None")

    def get_window_titles_info_related_via_win32gui(self) -> Optional[List[Tuple[str, int]]]:
        import logging

        from functions.get_windows_opened_with_hwnd import get_windows_opened_with_hwnd
        from objects.pk_etc import PK_UNDERLINE
        from sources.objects.pk_local_test_activate import LTA

        logging.debug(PK_UNDERLINE)

        while True:
            all_titles = get_windows_opened_with_hwnd()
            found_windows = []
            logging.debug(f'''len(found_windows)={len(found_windows)} {'%%%FOO%%%' if LTA else ''}''')  # {'%%%FOO%%%' if LTA else ''}  func_n 이 아닌 caller_n 이 logging 되기 때문에 요긴할때가 있다. 그리도 비추.
            if len(found_windows) >= 1:
                break
            # 정확한 매칭 로직
            for title, hwnd in all_titles:
                # pk_*
                title_reference = self.get_window_title_loaded_reference()
                compare_result = "일치" if len(title_reference) == len(title) else "불일치"
                compare_title = f"'{title_reference}' 와 '{title}' 창 제목 길이비교결과"
                compare_condition = rf"{len(title_reference)}와 {len(title)}는"
                logging.debug(f"{compare_title}, {compare_condition} {compare_result}")
                if compare_result == '일치':
                    found_windows.append((title, hwnd))
                    return found_windows if found_windows else None
            ensure_slept(milliseconds=80)

    def get_window_title_loaded_reference(self):
        from sources.functions.get_nx import get_nx
        from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_LOSSLESSCUT_EXE
        if self.f_video_to_load is None:
            logging.debug("로드할 비디오가 없습니다.")
            ensure_pnx_opened_by_ext(self.d_working)
            ensure_console_paused(text="로드할 비디오가 없습니다.")

        window_title_loaded_reference = None
        if self.f_video_player == F_LOSSLESSCUT_EXE:
            window_title_loaded_reference = f'{get_nx(self.f_video_to_load)} - LosslessCut'
        elif self.f_video_player == F_POT_PLAYER:
            window_title_loaded_reference = f'{get_nx(self.f_video_to_load)} - 팟플레이어'
        else:
            window_title_loaded_reference = "not defined refence window title"
        return window_title_loaded_reference.strip()  # task_orchestrator_cli_option : strip() 처리 " f.mp4" 인경우 재생 안되는 문제

    def get_window_title_and_hwnd_loaded_at_video_player(self) -> Optional[Tuple[str, int]]:
        import logging
        import traceback

        from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
        from functions.get_windows_opened_with_hwnd import get_windows_opened_with_hwnd

        try:
            titles_with_hwnds = get_windows_opened_with_hwnd()
            for title, hwnd in titles_with_hwnds:

                title_reference = self.get_window_title_loaded_reference()
                if title_reference is None:
                    logging.debug(rf"title_reference is None, title={title} hwnd={hwnd}")
                    return None
                compare_result = "일치" if len(title_reference) == len(title) else "불일치"
                compare_title = f"'{title_reference}' 와 '{title}' 창 제목 길이비교결과"
                compare_condition = rf"{len(title_reference)}와 {len(title)}는"
                logging.debug(f"{compare_title}, {compare_condition} {compare_result}")

                if title == self.get_window_title_loaded_reference():
                    return title, hwnd  # 첫 번째로 찾은 '로드된' 창의 정보 반환

            return None
        except:
            ensure_debug_loged_verbose(traceback)
            return None

    def ensure_focus_on(self, hwnd):

        import win32gui
        import win32con
        win32gui.SetForegroundWindow(hwnd)
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

    def ensure_video_player_play_button_pressed(self):

        """LosslessCut 창들 중 비디오 로딩이 완료된 창을 찾아 재생 버튼을 누릅니다."""
        from sources.functions.ensure_pressed import ensure_pressed
        from sources.functions.ensure_slept import ensure_slept
        import logging

        try:
            window_info = self.get_window_title_and_hwnd_loaded_at_video_player()
            if not window_info:
                logging.info(f"재생할 {self.f_video_player} 창을 찾을 수 없습니다.")
                return False

            title, hwnd = window_info
            logging.debug(f"video_player={self.f_video_player}")
            logging.debug(f"title={title}")
            logging.debug(f"hwnd={hwnd}")

            self.ensure_focus_on(hwnd)
            ensure_slept(milliseconds=80)

            ensure_pressed("space")
            logging.debug(f"'{title}' 창에 스페이스바 재생 입력 완료")

            return True

        except:
            logging.error(f"재생 함수 실행 중 오류")
            ensure_debug_loged_verbose(traceback)
            return False

    @ensure_seconds_measured
    def ensure_video_player_screen_maximized(self):

        from sources.functions.ensure_window_maximized_like_human import ensure_window_maximized_like_human
        from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_LOSSLESSCUT_EXE

        from sources.functions.ensure_pressed import ensure_pressed
        from sources.functions.ensure_slept import ensure_slept
        import logging
        try:
            window_info = self.get_window_title_and_hwnd_loaded_at_video_player()

            if not window_info:
                logging.info(f"최대화할 {self.f_video_player} 창을 찾을 수 없습니다.")
                return False

            title, hwnd = window_info
            logging.debug(f"video_player={self.f_video_player} title='{title}' handle={hwnd}")

            self.ensure_focus_on(hwnd)
            ensure_slept(milliseconds=80)

            if self.f_video_player == F_LOSSLESSCUT_EXE:
                ensure_window_maximized_like_human()
            elif self.f_video_player == F_POT_PLAYER:
                key_to_press = "enter"
                ensure_pressed(key_to_press)
                # ensure_slept(milliseconds=80)
                # ensure_pressed(key_to_press)

            logging.debug(f"'{title}' 창에 스페이스바 재생 입력 완료")

            return True

        except:
            logging.error(f"재생 함수 실행 중 오류")
            ensure_debug_loged_verbose(traceback)
            return False

    def reset_play_state(self):

        """비디오 재생 관련 상태를 모두 초기화합니다."""
        self.current_video_loaded = False
        self.current_video_played = False
        self.played_window = False
        self.current_video_play_time = None
        self.play_retry_count = 0
        self.play_attempted = False
        self.reload_needed = False
        self.current_window_title = None
        self.extracted_filename = None
        self.window_title_analysis_time = None
        for state in self.window_titles_by_state:
            self.window_titles_by_state[state] = []
        self.state_change_history = []

    def update_state(self, new_state: str):
        import logging

        if new_state != self.current_state:
            logging.debug(f"[STATE_CHANGE] {self.current_state} → {new_state}")
            self.prev_state = self.current_state
            self.current_state = new_state

            if new_state == "EXPORTING":
                self.export_detected = True
                self.reload_needed = True
            elif new_state == "FILE_LOADED" and self.export_detected:
                self.play_attempted = False
                self.export_detected = False
            elif new_state == "IDLE" and self.prev_state == "EXPORTING":
                self.reload_needed = True

    def mark_video_played(self):
        import logging

        self.current_video_played = True
        self.played_window = True
        self.play_attempted = True
        self.current_video_play_time = None
        video_name = self.f_video_to_load.name if self.f_video_to_load else 'Unknown'
        logging.debug(f"[PLAY_STATE] 비디오 재생 완료: {video_name}")

    def attempt_play(self):
        import logging

        import time
        self.play_retry_count += 1
        self.current_video_play_time = time.time()
        self.play_attempted = True
        video_name = self.f_video_to_load.name if self.f_video_to_load else 'Unknown'
        logging.debug(f"[PLAY_STATE] 재생 시도 {self.play_retry_count}/{self.max_play_retries}: {video_name}")

    def get_play_status_summary(self) -> str:

        play_status = (
            f"로드: {self.current_video_loaded}, "
            f"재생: {self.current_video_played}, "
            f"창재생: {self.played_window}, "
            f"시도: {self.play_retry_count}/{self.max_play_retries}"
        )
        window_analysis = self.get_window_analysis_summary()
        state_summary = self.get_state_summary()
        return f"{play_status} | {window_analysis} | {state_summary}"

    def get_window_analysis_summary(self) -> str:

        if not self.current_window_title:
            return "창 제목 분석 없음"
        analysis_info = f"창 제목: '{self.current_window_title}'"
        if self.extracted_filename:
            analysis_info += f", 추출된 파일명: '{self.extracted_filename}'"
        if self.window_title_analysis_time:
            import time
            elapsed = time.time() - self.window_title_analysis_time
            analysis_info += f", 분석 시간: {elapsed:.1f}초 전"
        return analysis_info

    def get_state_summary(self) -> str:

        summary = []
        for state, titles in self.window_titles_by_state.items():
            if titles:
                summary.append(f"{state}: {len(titles)}개")
        return " | ".join(summary) if summary else "감지된 창 없음"

    def ensure_video_file_loaded_on_video_player(self, video_to_play):
        import logging
        import time
        from pathlib import Path

        from functions.ensure_command_executed_advanced_async import ensure_command_executed_advanced_async
        from sources.functions import ensure_slept
        from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_LOSSLESSCUT_EXE

        import traceback

        from sources.functions.ensure_command_executed import ensure_command_executed
        from sources.functions.ensure_pressed import ensure_pressed

        # if video_to_play is None:
        #     self.update_video_to_load(self.d_working)
        #     video_to_play = self.f_video_to_load

        video = video_to_play
        player = self.f_video_player
        try:
            if video is None:
                logging.debug(f"비디오 파일 로드불가 video is None")
                return False

            if video is not None:
                if Path(video).exists():
                    if player == F_LOSSLESSCUT_EXE:
                        ensure_command_executed(cmd=rf'''start "" "{player}" "{video}"''')
                    elif player == F_POT_PLAYER:
                        # ensure_command_executed(cmd=rf'cmd /c start "" "{player}" "{video}"') # fail : played but, lock
                        # ensure_command_executed(cmd=rf'cmd /c start "" "{player}" "{video}"', mode='a') # fail
                        # ensure_command_executed(cmd=rf'''start "" "{player}" "{video}"''') # fail : played but, lock
                        # ensure_command_executed(cmd=rf'''start "" "{player}" "{video}"''', mode='a') # fail
                        ensure_command_executed_advanced_async(cmds=[Path(player), Path(video)])  # success

                    ensure_slept(milliseconds=80)

                    # Loading file - LosslessCut 처리
                    if self.f_video_player == F_LOSSLESSCUT_EXE:
                        title_info = self.get_window_titles_info_related_via_win32gui()
                        for title, hwnd in title_info:
                            logging.info(f"title={title} hwnd={hwnd}")
                            if title == 'Loading file - LosslessCut':
                                logging.info(f"import 팝업 감지")
                                self.ensure_focus_on(hwnd)
                                ensure_pressed("esc")
                                logging.debug(f"import 팝업 창을 닫았습니다")
                                ensure_slept(milliseconds=80)
                                break
                    ensure_slept(milliseconds=80)

                    # check loaded
                    loop_miliseconds_limit = 10000
                    time_s = time.time()
                    while True:
                        elapsed = time_s - time.time()
                        if loop_miliseconds_limit < elapsed:
                            logging.debug(f"비디오 로드 실패: {video}")
                            return False
                        if not self.is_loaded():
                            ensure_slept(milliseconds=80)
                            continue
                        else:
                            logging.debug(f"비디오 로드 성공: {video}")
                            return True
                else:
                    logging.debug(f"로드할 비디오 파일이 존재하지 않습니다: {video}")
        except:
            ensure_debug_loged_verbose(traceback)
            raise

    def is_video_player_running(self):
        import logging

        from functions.is_empty_std_output_streams import is_empty_std_output_streams
        from sources.functions.ensure_command_executed import ensure_command_executed

        from sources.functions.get_nx import get_nx

        f_video_player_tasklist_name = None
        f_video_player = self.f_video_player
        f_video_player_tasklist_name = get_nx(f_video_player)

        soss = ensure_command_executed(cmd=f'tasklist.exe | findstr "{f_video_player_tasklist_name}"')
        if is_empty_std_output_streams(soss):
            logging.debug(f"{get_nx(f_video_player)} is not running")
            return False
        logging.debug(f"{get_nx(f_video_player)} is running")
        return True

    def ensure_video_player_reopened(self):

        from sources.functions.get_nx import get_nx

        from sources.functions import ensure_slept

        from sources.functions.ensure_command_executed import ensure_command_executed
        import logging

        self.kill_video_player()
        while 1:
            if not self.is_video_player_running():
                logging.debug(f"Attempting to launch {get_nx(self.f_video_player)}")
                cmd = rf'''start "" "{self.f_video_player}"'''
                # cmd = rf'''start "" /MIN "{F_VIDEO_FILE}"'''
                ensure_command_executed(cmd=cmd, mode='a')
                while 1:
                    if self.is_video_player_running():
                        return True
                    ensure_slept(milliseconds=88)

    def kill_video_player(self):

        import logging
        from sources.functions.ensure_command_executed import ensure_command_executed
        from sources.functions.get_nx import get_nx
        f_video_player = self.f_video_player
        ensure_command_executed(cmd=f'taskkill.exe /im {get_nx(f_video_player)} /f')
        logging.debug(f"{get_nx(f_video_player)} is killed")

    def get_d_working_from_routine(self):

        from functions.ensure_value_completed_advanced import ensure_value_completed_advanced
        from functions.get_caller_n import get_caller_n

        from pathlib import Path

        from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING, D_G_DRIVE_PK_WORKING

        # task_orchestrator_cli_option
        key_name = "d_working"
        func_n = get_caller_n()
        # func_n = "ensure_video_played_at_video_player"
        options = [Path(p) for p in [D_G_DRIVE_PK_WORKING, D_PK_WORKING]]
        selected = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=list(set(options)), editable=False)
        d_working = selected
        return d_working

    def is_video_loaded_already(self, loop_cnt):
        import logging

        from sources.functions.get_nx import get_nx

        window_info = self.get_window_title_and_hwnd_loaded_at_video_player()

        if window_info:
            title, hwnd = window_info

            title_reference = self.get_window_title_loaded_reference()
            compare_result = "일치" if len(title_reference) == len(title) else "불일치"
            compare_title = f"'{title_reference}' 와 '{title}' 창 제목 길이비교결과"
            compare_condition = rf"{len(title_reference)}와 {len(title)}는"
            logging.debug(f"{compare_title}, {compare_condition} {compare_result}")

            logging.info(f"비디오가 로드된 {get_nx(self.f_video_player)} 창이 있습니다 ({title}) handle={hwnd}")
            if loop_cnt == 0:
                self.ensure_focus_on(hwnd)
            return True

        logging.info(f"비디오가 로드된 {get_nx(self.f_video_player)} 창이 없습니다")
        logging.info(f"비디오가 로드 재시도")
        return False

    def ensure_video_player_idle_window_title_monitored(self):
        import logging

        from sources.functions import ensure_slept

        from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
        title = "LosslessCut"
        while 1:
            logging.debug(rf"{title} is monitoring...")
            if not self.is_video_player_running():
                self.ensure_video_player_reopened()
            if is_window_opened_via_window_title(window_title=title):
                logging.debug(rf"{title} is monitored")
                break
            else:
                ensure_slept(milliseconds=80)

    def ensure_video_toogled_between_pause_and_play(self):

        from sources.functions.ensure_pressed import ensure_pressed
        from sources.functions.ensure_window_to_front import ensure_window_to_front

        ensure_window_to_front(window_title_seg=self.get_window_title_loaded_reference())
        ensure_pressed("space")
        self.is_video_playing = True

    def is_video_played(self):

        return self.is_video_playing

    def is_loaded(self):
        import logging

        from functions.get_windows_opened import get_windows_opened

        for title in get_windows_opened():

            title_reference = self.get_window_title_loaded_reference()
            compare_result = "일치" if len(title_reference) == len(title) else "불일치"
            compare_title = f"'{title_reference}' 와 '{title}' 창 제목 길이비교결과"
            compare_condition = rf"{len(title_reference)}와 {len(title)}는"
            logging.debug(f"{compare_title}, {compare_condition} {compare_result}")

            if title == self.get_window_title_loaded_reference():
                return True
        return False
