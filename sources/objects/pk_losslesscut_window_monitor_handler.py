import logging
import threading
import time
from sources.objects.pk_event_system import Event, EventType, EventHandler, EventSystemManager, create_event, EventQueue
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions import ensure_slept

class LosslessCutWindowMonitorHandler(EventHandler):
    def __init__(self, event_queue: EventQueue, video_player_instance):
        super().__init__(event_queue, name="LosslessCutWindowMonitorHandler")
        self.video_player = video_player_instance
        self._monitoring_thread = None
        self._running = False

    def register_handlers(self):
        self.event_queue.register_handler(EventType.WINDOW_TITLE_LOSSLESSCUT_IDLE_NAME_MATCHED, self.on_losslesscut_window_matched)

    def on_losslesscut_window_matched(self, event: Event):
        logging.info(f"이벤트 수신: {event.type.name}. LosslessCut 창이 감지되었습니다. 비디오 재생 로직을 실행합니다.")
        from sources.functions.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
        ensure_video_played_at_losslesscut(self.video_player)

    def _monitor_loop(self):
        logging.info("LosslessCut 창 모니터링 스레드 시작.")
        while self._running:
            if is_window_opened_via_window_title(window_title="LosslessCut"):
                logging.debug("LosslessCut 창 감지. 이벤트 발생.")
                event = create_event(
                    event_type=EventType.WINDOW_TITLE_LOSSLESSCUT_IDLE_NAME_MATCHED,
                    data={"window_title": "LosslessCut"},
                    source="LosslessCutWindowMonitorHandler"
                )
                self.event_queue.add_event(event)
                ensure_slept(milliseconds=5000)
            else:
                logging.debug("LosslessCut 창 아직 감지되지 않음. 대기 중...")
                ensure_slept(milliseconds=500)

    def start_monitoring(self):
        if not self._running:
            self._running = True
            self._monitoring_thread = threading.Thread(target=self._monitor_loop, daemon=True)
            self._monitoring_thread.start()
            logging.info("LosslessCut 창 모니터링 시작됨.")

    def stop_monitoring(self):
        if self._running:
            self._running = False
            if self._monitoring_thread and self._monitoring_thread.is_alive():
                self._monitoring_thread.join(timeout=1.0)
            logging.info("LosslessCut 창 모니터링 중지됨.")