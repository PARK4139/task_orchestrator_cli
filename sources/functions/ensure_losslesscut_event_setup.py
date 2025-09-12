import logging
import time
import threading
from enum import IntFlag, auto

from sources.functions import ensure_slept
from sources.functions.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.objects.pk_event_system import Event, EventType, EventSystemManager, create_event, EventQueue
from sources.objects.pk_losslesscut_window_monitor_handler import LosslessCutWindowMonitorHandler
from sources.objects.pk_video_player import PkVideoPlayer


class _SetupOps(IntFlag):
    AS_VOID = auto()
    AS_LOOP = auto()
    AS_EVENT = auto()


def _ensure_executed_by_following_setup(setup_op: "_SetupOps", video_player: PkVideoPlayer) -> None:
    from objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE

    if video_player is None:
        video_player = PkVideoPlayer(f_video_player=F_LOSSLESSCUT_EXE)

    if setup_op & _SetupOps.AS_VOID:
        ensure_video_played_at_losslesscut(video_player)

    if setup_op & _SetupOps.AS_LOOP:
        loop_cnt = 0
        while 1:
            ensure_video_played_at_losslesscut(video_player, loop_cnt)
            loop_cnt += 1
            ensure_slept(milliseconds=5000)

    if setup_op & _SetupOps.AS_EVENT:
        logging.info("이벤트 기반 시스템을 시작합니다...")
        main_pk_event_system = EventSystemManager()
        losslesscut_monitor_handler = LosslessCutWindowMonitorHandler(main_pk_event_system.event_queue, video_player)
        main_pk_event_system.add_handler(losslesscut_monitor_handler)
        main_pk_event_system.start()
        losslesscut_monitor_handler.start_monitoring()
        logging.info("창 제목 LosslessCut 매칭 이벤트 감지 대기 중... (Ctrl+C로 종료)")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logging.info("사용자에 의해 시스템이 중지됩니다.")
        finally:
            losslesscut_monitor_handler.stop_monitoring()
            main_pk_event_system.stop()
