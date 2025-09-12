import threading
from dataclasses import dataclass
from typing import Callable, Optional, Dict, Any

from functions.ensure_losslescut_killed import ensure_losslescut_killed
from functions.ensure_potplayer_killed import ensure_potplayer_killed


@dataclass
class TimeRange:
    """시간 구간 데이터 클래스"""
    start_time: str
    end_time: str
    duration_minutes: int
    routine_name: str
    routine_func: Callable
    executed: bool = False


class PkRoutineScheduler:
    """스케줄링의 모든 로직과 데이터를 캡슐화한 싱글턴 클래스"""

    _instance: Optional['PkRoutineScheduler'] = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):

        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, state_file_path: Optional[str] = None, speak_mode: bool = True):

        from functions.ensure_routine_startup_enabled import ensure_routine_startup_enabled

        from objects.task_orchestrator_cli_directories import D_DOWNLOADED_FROM_TORRENT
        from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE, F_POT_PLAYER
        from sources.objects.pk_video_player import PkVideoPlayer

        import asyncio
        import datetime
        import threading
        from pathlib import Path
        from typing import List, Optional

        import logging

        is_initialized = hasattr(self, '_initialized') and self._initialized
        settings_changed = False
        if is_initialized:
            if self.state_file_path != state_file_path or self.speak_mode != speak_mode:
                settings_changed = True
                logging.info("스케줄러 설정이 변경되어 재초기화를 진행합니다.")
                if self.is_running:
                    self.stop()

        if not is_initialized or settings_changed:
            self.speak_mode = speak_mode

            if state_file_path:
                self.state_file_path = Path(state_file_path)
            else:
                from sources.objects.task_orchestrator_cli_files import F_SCHEDULER_STATE
                self.state_file_path = F_SCHEDULER_STATE

            self.time_ranges: List[TimeRange] = []
            self.current_routine: Optional[TimeRange] = None
            self.is_running = False
            self.demo_start_time: Optional[datetime.datetime] = None
            self.loop: Optional[asyncio.AbstractEventLoop] = None
            self.thread: Optional[threading.Thread] = None
            self.completion_logger: Optional[logging.Logger] = None
            self._initialized = True
            self.define_routines()
            logging.info(f"PkRoutineScheduler가 초기화되었습니다, 음성: {self.speak_mode}, 상태파일: {self.state_file_path})")
            if self.speak_mode:
                from sources.functions.ensure_spoken import ensure_spoken
                from sources.functions.ensure_losslescut_killed import ensure_losslescut_killed

                from sources.functions.ensure_potplayer_killed import ensure_potplayer_killed

                # pk_* : pk_scheduler entry point
                ensure_spoken("스케줄러가 시작되었습니다.")

                ensure_potplayer_killed()
                ensure_losslescut_killed()
                # ensure_process_killed_by_image_name('chrome.exe')
                # ensure_process_killed_by_image_name('code.exe')
                # ensure_process_killed_by_image_name('cursor.exe')
                # ensure_gemini_cli_killed()
                # ensure_cmd_exe_killed()
                # ensure_windows_deduplicated()

                # initialize video_player
                # d_working = Path('G:\Downloads\pk_working')
                d_working = D_DOWNLOADED_FROM_TORRENT
                self.losslesscut_mgr = PkVideoPlayer(f_video_player=F_LOSSLESSCUT_EXE, d_working=d_working)
                self.potplayer_mgr = PkVideoPlayer(f_video_player=F_POT_PLAYER, d_working=d_working)
                # self.potplayer.ensure_video_player_reopened()

                # ensure_python_file_enabled_advanced(file_path=D_TASK_ORCHESTRATOR_CLI_WRAPPERS / 'pk_ensure_task_orchestrator_cli_log_editable.py')
                ensure_routine_startup_enabled()

        logging.info("========== 등록된 스케줄 ==========")
        for start, end, name, _ in self.schedule_config:
            logging.info(f"- {start} ~ {end}: {name}")
        logging.info("===================================")

    def define_routines(self):

        from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
        from functions.ensure_os_locked_at_sleeping_time import ensure_os_locked_at_sleeping_time

        import traceback

        import logging

        from sources.functions.ensure_spoken import ensure_spoken
        from sources.functions.ensure_slept import ensure_slept
        from sources.functions.ensure_sound_track_played import ensure_sound_track_played
        from sources.functions.ensure_window_to_front_of_pycharm import ensure_pycharm_window_to_front

        """클래스 내부에서 루틴 함수와 스케줄을 정의합니다."""

        @self._routine_decorator
        def do_routine_rest():
            from functions.ensure_potplayer_killed import ensure_potplayer_killed
            try:
                self.speak_routine_start(self.current_routine.routine_name)

                ensure_potplayer_killed()

                # 비디오 이어서 재생
                if self.losslesscut_mgr.current_state == "not_initialized":
                    self.losslesscut_mgr.ensure_video_player_reopened()
                if not self.losslesscut_mgr.is_video_loaded_already(loop_cnt=0):
                    self.losslesscut_mgr.ensure_video_file_loaded_on_video_player(video_to_play=self.losslesscut_mgr.f_video_to_load)
                self.losslesscut_mgr.ensure_video_player_play_button_pressed()
                self.losslesscut_mgr.ensure_video_player_screen_maximized()

                if not self.potplayer_mgr.is_video_loaded_already(loop_cnt=0):
                    self.potplayer_mgr.ensure_video_file_loaded_on_video_player(video_to_play=self.potplayer_mgr.f_video_to_load)
                self.potplayer_mgr.ensure_video_player_play_button_pressed()
                self.potplayer_mgr.ensure_video_player_screen_maximized()


            except:
                ensure_debug_loged_verbose(traceback)

        @self._routine_decorator
        def do_routine_dinner():
            try:
                self.speak_routine_start(self.current_routine.routine_name)

                # 즐거운노래
                ensure_sound_track_played()
                ensure_slept(milliseconds=80)

            except:
                ensure_debug_loged_verbose(traceback)

        @self._routine_decorator
        def do_routine_go_to_sleep():
            try:
                self.speak_routine_start(self.current_routine.routine_name)

                # 즐거운노래
                ensure_sound_track_played()
                ensure_slept(milliseconds=80)

                ensure_os_locked_at_sleeping_time()


            except:
                ensure_debug_loged_verbose(traceback)

        @self._routine_decorator
        def do_routine_work():
            try:
                self.speak_routine_start(self.current_routine.routine_name)
                # self._ensure_resource_not_necessary_to_routine_removed()

                # video stop
                # if self.lossclescut.is_video_played():
                #     self.lossclescut.ensure_video_toogled_between_pause_and_play()
                #
                # if self.potplayer.is_video_played():
                #     self.potplayer.ensure_video_toogled_between_pause_and_play()
                ensure_losslescut_killed()
                ensure_potplayer_killed()
                # ensure_slept(milliseconds=80) # TODO loop 함수 만들어서 조건 충족하지 못하면 10 milliseconds slept 하는 쪽이 속도면에서는 빠를것. 다만 CPU 측면에서는 많은 리소스를 사용해야 할것임.

                # 노동요
                ensure_sound_track_played()
                ensure_slept(milliseconds=80)

                # 코드 작성 작업
                ensure_pycharm_window_to_front()

            except:
                ensure_debug_loged_verbose(traceback)

        @self._routine_decorator
        def do_routine_lunch():
            try:
                self.speak_routine_start(self.current_routine.routine_name)
            except:
                ensure_debug_loged_verbose(traceback)

        @self._routine_decorator
        def do_routine_exercise():
            try:
                self.speak_routine_start(self.current_routine.routine_name)
                ensure_spoken("테니스공 활용 카프레이즈, 33회")
                logging.debug("테니스공 활용 카프레이즈, 33회")
            except:
                ensure_debug_loged_verbose(traceback)

        @self._routine_decorator
        def do_routine_morning_prep():
            try:
                self.speak_routine_start(self.current_routine.routine_name)
            except:
                ensure_debug_loged_verbose(traceback)

        @self._routine_decorator
        def do_routine_afternoon_prep():
            try:
                self.speak_routine_start(self.current_routine.routine_name)
                ensure_spoken("오후 주간 작업 준비 완료")
                logging.debug("오후 주간 작업 준비 완료")
            except:
                ensure_debug_loged_verbose(traceback)

        @self._routine_decorator
        def do_routine_evening_prep():
            try:
                self.speak_routine_start(self.current_routine.routine_name)
            except:
                ensure_debug_loged_verbose(traceback)

        self.schedule_config = [
            ("07:00", "07:10", "오전작업전준비", do_routine_morning_prep),
            ("07:10", "07:40", "작업시간", do_routine_work),
            ("07:40", "07:45", "휴식시간", do_routine_rest),
            ("07:45", "08:15", "작업시간", do_routine_work),
            ("08:15", "08:20", "휴식시간", do_routine_rest),
            ("08:20", "08:50", "작업시간", do_routine_work),
            ("08:50", "08:55", "휴식시간", do_routine_rest),
            ("08:55", "09:25", "작업시간", do_routine_work),
            ("09:25", "09:30", "휴식시간", do_routine_rest),
            ("09:30", "10:00", "작업시간", do_routine_work),
            ("10:00", "10:05", "휴식시간", do_routine_rest),
            ("10:05", "10:35", "작업시간", do_routine_work),
            ("10:35", "10:40", "휴식시간", do_routine_rest),
            ("10:40", "11:10", "작업시간", do_routine_work),
            ("11:10", "11:15", "휴식시간", do_routine_rest),
            ("11:15", "11:40", "작업시간", do_routine_work),
            ("11:40", "12:40", "운동시간", do_routine_exercise),
            ("12:40", "14:00", "점심시간", do_routine_lunch),
            ("14:00", "14:10", "오후주간작업전준비", do_routine_afternoon_prep),
            ("14:10", "14:40", "작업시간", do_routine_work),
            ("14:40", "14:45", "휴식시간", do_routine_rest),
            ("14:45", "15:15", "작업시간", do_routine_work),
            ("15:15", "15:20", "휴식시간", do_routine_rest),
            ("15:20", "15:50", "작업시간", do_routine_work),
            ("15:50", "15:55", "휴식시간", do_routine_rest),
            ("15:55", "16:25", "작업시간", do_routine_work),
            ("16:25", "16:30", "휴식시간", do_routine_rest),
            ("16:30", "17:00", "작업시간", do_routine_work),
            ("17:00", "17:05", "휴식시간", do_routine_rest),
            ("17:05", "17:35", "작업시간", do_routine_work),
            ("17:35", "17:40", "휴식시간", do_routine_rest),
            ("17:40", "17:45", "추가휴식시간", do_routine_rest),
            ("17:45", "18:10", "집으로 갈시간", do_routine_work),
            ("18:10", "18:15", "저녁시간", do_routine_dinner),
            ("18:15", "18:25", "오후야간작업전준비", do_routine_evening_prep),
            ("18:25", "18:55", "작업시간", do_routine_work),
            ("18:55", "19:00", "휴식시간", do_routine_rest),
            ("19:00", "19:30", "작업시간", do_routine_work),
            ("19:30", "19:35", "휴식시간", do_routine_rest),
            ("19:35", "20:05", "작업시간", do_routine_work),
            ("20:05", "20:10", "휴식시간", do_routine_rest),
            ("20:10", "20:40", "작업시간", do_routine_work),
            ("20:40", "20:45", "휴식시간", do_routine_rest),
            ("20:45", "21:00", "자야전휴식시간", do_routine_rest),
            ("21:00", "23:00", "자야할시간", do_routine_go_to_sleep),
            ("00:00", "05:00", "자야할시간", do_routine_go_to_sleep), #  세벽 루틴
        ]

    def speak_routine_start(self, routine_title: str):

        import datetime

        import logging

        if not self.speak_mode:
            return
        try:
            from sources.functions.ensure_spoken import ensure_spoken
        except ImportError:
            logging.warning("ensure_spoken import 실패")
            return

        logging.info(f"{routine_title} 루틴 실행")

        if self.current_routine:
            end_time_str = self.current_routine.end_time  # e.g., "07:10"
            duration = self.current_routine.duration_minutes

            # Convert "HH:MM" string to datetime object to format
            # We need a dummy date part to create a datetime object
            dummy_date = datetime.date.today()
            end_datetime = datetime.datetime.strptime(f"{dummy_date.strftime('%Y-%m-%d')} {end_time_str}", "%Y-%m-%d %H:%M")

            formatted_end_time = end_datetime.strftime("%H시 %M분")

            now_datetime = datetime.datetime.now()
            time_difference = end_datetime - now_datetime
            remaining_duration_minutes = max(0, int(time_difference.total_seconds() / 60))

            speech_text = f"{routine_title}, {formatted_end_time}까지, {remaining_duration_minutes}분간 진행해주세요"
        else:
            # Fallback if current_routine is not set (should not happen in normal flow)
            speech_text = f"{routine_title} 루틴 시작"
            logging.warning(f"current_routine이 설정되지 않아 {routine_title}에 대한 상세 음성 안내를 제공할 수 없습니다.")

        logging.debug(f"speech_text='{speech_text}'")
        ensure_spoken(speech_text)

    def _routine_decorator(self, func: Callable) -> Callable:

        from functools import wraps

        """루틴 함수에 공통 로직(완료 로깅)을 적용하는 데코레이터"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if self.completion_logger:
                self.completion_logger.info(f"루틴 실행 완료: {func.__name__}")
            return result

        return wrapper

    def _setup_completion_logger(self):

        from pathlib import Path

        import logging

        if not self.demo_start_time:
            return
        try:
            from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_LOGS
        except ImportError:
            logging.warning("D_TASK_ORCHESTRATOR_CLI_LOGS import 실패")
            return

        start_time_str = self.demo_start_time.strftime('%Y_%m_%d_%H%M%S')
        log_filename = Path(D_TASK_ORCHESTRATOR_CLI_LOGS) / f"pk_schedule_executed_at_{start_time_str}.log"
        logger = logging.getLogger(f'routine_completion_{id(self)}')
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        if not logger.handlers:
            handler = logging.FileHandler(log_filename, encoding='utf-8')
            formatter = logging.Formatter('%(asctime)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        self.completion_logger = logger

    def _load_execution_state(self) -> set:
        import json
        from datetime import date

        try:
            if self.state_file_path.exists():
                with open(self.state_file_path, 'r', encoding='utf-8') as f:
                    state_data = json.load(f)
                today_str = str(date.today())
                return {name for name, exec_date in state_data.items() if exec_date == today_str}
        except (IOError, json.JSONDecodeError):
            return set()
        return set()

    def _save_execution_state(self, routine_name: str):
        import traceback

        from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose

        import json
        from datetime import date

        import logging

        try:
            try:
                if self.state_file_path.exists():
                    with open(self.state_file_path, 'r', encoding='utf-8') as f:
                        state_data = json.load(f)
                else:
                    state_data = {}
            except (IOError, json.JSONDecodeError):
                state_data = {}

            today_str = str(date.today())
            state_data[routine_name] = today_str

            with open(self.state_file_path, 'w', encoding='utf-8') as f:
                json.dump(state_data, f, indent=4)
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"루틴 상태 파일 저장 실패")
            ensure_debug_loged_verbose(traceback)

    def _prepare_routines(self):

        import datetime

        self.time_ranges.clear()
        # Always reset executed status on scheduler startup to ensure routines run.
        for start, end, name, func in self.schedule_config:
            time_format = "%H:%M"
            start_time = datetime.datetime.strptime(start, time_format)
            end_time = datetime.datetime.strptime(end, time_format)
            duration_minutes = int((end_time - start_time).total_seconds() / 60)
            time_range = TimeRange(start, end, duration_minutes, name, func)
            time_range.executed = False  # Force executed to False on startup
            self.time_ranges.append(time_range)

    def _ensure_resource_not_necessary_to_routine_removed(self):

        # 작업루틴에 불 필요한 리소스 제거
        # from sources.functions import ensure_slept

        # ensure_slept(milliseconds=80)
        # ensure_potplayer_killed()
        # ensure_slept(milliseconds=80)
        pass

    def get_current_time_range(self) -> Optional[TimeRange]:

        import datetime

        """현재 시간에 맞는 루틴을 찾습니다"""
        now = datetime.datetime.now()

        # 실제 모드: 현재 시간으로 계산
        current_time_str = now.strftime("%H:%M")
        for time_range in self.time_ranges:
            if time_range.start_time <= current_time_str < time_range.end_time:
                return time_range
        return None

    async def _execute_routine(self, time_range: TimeRange):
        import traceback

        from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose

        import asyncio

        import logging

        logging.debug(f"Attempting to execute: {time_range.routine_name}, initial executed: {time_range.executed}")
        if time_range.executed:
            logging.debug(f"Routine {time_range.routine_name} already executed, returning.")
            return
        try:
            logging.info(f"루틴 실행 시작: {time_range.routine_name}")
            logging.debug(f"Calling routine={time_range.routine_func.__name__}()")
            await asyncio.get_event_loop().run_in_executor(None, time_range.routine_func)
            logging.debug(f"Routine function {time_range.routine_func.__name__} completed.")
            time_range.executed = True
            logging.debug(f"Set {time_range.routine_name}.executed to True.")
            self._save_execution_state(time_range.routine_name)
            logging.debug(f"Saved execution state for {time_range.routine_name}.")
        except:
            logging.error(f"루틴 실행 실패 {time_range.routine_name}")
            ensure_debug_loged_verbose(traceback)

    async def _main_loop(self):
        import traceback

        from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose

        import asyncio
        import datetime

        import logging

        while self.is_running:
            try:
                current_range = self.get_current_time_range()

                # Debugging: Log current_range and self.current_routine
                # logging.debug(f"current_range: {current_range.routine_name if current_range else 'None'}, executed: {current_range.executed if current_range else 'N/A'}")
                # logging.debug(f"self.current_routine: {self.current_routine.routine_name if self.current_routine else 'None'}")

                # Update current_routine if it has changed
                if current_range != self.current_routine:
                    if current_range:
                        now = datetime.datetime.now()
                        current_time_str = now.strftime("%H:%M:%S")
                        logging.info(f"현재 루틴 변경: {current_range.routine_name} ({current_range.start_time}-{current_range.end_time}) - 현재 시간: {current_time_str} - 함수: {current_range.routine_func.__name__}")
                    self.current_routine = current_range

                # Attempt to execute the current routine if it exists and hasn't been executed today
                if current_range and not current_range.executed:
                    logging.debug(f"Executing routine: {current_range.routine_name}, executed status: {current_range.executed}")
                    await self._execute_routine(current_range)
                else:
                    # logging.debug(f"Not executing routine. current_range: {current_range.routine_name if current_range else 'None'}, executed: {current_range.executed if current_range else 'N/A'}")
                    pass

                # pk_option
                # await asyncio.sleep(1)
                await asyncio.sleep(20)  # 부하를 줄이기 위해 sleep time 을 1에서 20으로 증가
                # logging.debug(f"pk_scheduler loop is working")
            except:
                ensure_debug_loged_verbose(traceback)
                await asyncio.sleep(5)

    def _run_in_thread(self):
        import traceback

        from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose

        import asyncio
        import datetime

        import logging

        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.is_running = True
        if not self.demo_start_time:
            self.demo_start_time = datetime.datetime.now()
        self._setup_completion_logger()
        try:
            self.loop.run_until_complete(self._main_loop())
        except RuntimeError as e:
            if "Event loop stopped before Future completed" in str(e):
                logging.debug("이벤트 루프가 정상적으로 중지되었습니다.")
            else:
                logging.error(f"스케줄러 스레드에서 예기치 않은 런타임 오류 발생")
                ensure_debug_loged_verbose(traceback)

    def start(self):

        import threading

        import logging

        if self.thread and self.thread.is_alive():
            logging.info("기존 스케줄러 스레드를 중지하고 재시작합니다.")
            self.stop()

        self._prepare_routines()
        self.thread = threading.Thread(target=self._run_in_thread, daemon=True)
        self.thread.start()

    def stop(self):

        import logging

        if not self.is_running:
            return
        self.is_running = False
        if self.loop:
            self.loop.call_soon_threadsafe(self.loop.stop)
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=2)
        logging.info("스케줄러가 중지되었습니다.")

    def get_status(self) -> Dict[str, Any]:

        progress = {}
        # if self.demo_mode and self.demo_start_time:
        #     elapsed_seconds = (datetime.datetime.now() - self.demo_start_time).total_seconds()
        #     total_duration_minutes = sum(r.duration_minutes for r in self.time_ranges)
        #     total_duration_seconds_in_demo = total_duration_minutes / 10
        #
        #     progress_percent = min(100, (elapsed_seconds / total_duration_seconds_in_demo) * 100) if total_duration_seconds_in_demo > 0 else 0
        #     progress = {
        #         "elapsed_seconds": elapsed_seconds,
        #         "total_duration_in_demo_seconds": total_duration_seconds_in_demo,
        #         "progress_percent": progress_percent,
        #     }

        return {
            "is_running": self.is_running,
            "current_routine": self.current_routine.routine_name if self.current_routine else None,
            "total_ranges": len(self.time_ranges),
            "executed_ranges": sum(1 for r in self.time_ranges if r.executed),
            "speak_mode": self.speak_mode,
            "state_file": str(self.state_file_path),
            "demo_progress": progress
        }


def get_pk_scheduler(state_file_path: Optional[str] = None, speak_mode: bool = True) -> PkRoutineScheduler:
    """스케줄러 싱글턴 인스턴스를 반환합니다. 설정 변경 시 재초기화합니다."""
    instance = PkRoutineScheduler(state_file_path=state_file_path, speak_mode=speak_mode)
    return instance
