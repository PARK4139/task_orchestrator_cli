import logging
from pathlib import Path

from pynput import mouse

from functions import ensure_spoken
from functions.ensure_mouse_coordination_history_reset import ensure_mouse_coordination_history_reset
from functions.ensure_mouse_moved import ensure_mouse_moved
from functions.get_env_var_name_id import get_env_var_id
from sources.objects.pk_event_system import EventSystemManager, EventType, create_event
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE

# 전역 이벤트 시스템 인스턴스 (또는 필요에 따라 주입)
# EventSystemManager는 싱글톤 패턴으로 관리되거나, 애플리케이션 시작 시 한 번만 인스턴스화되어야 합니다.
# 여기서는 모듈 레벨에서 인스턴스화하고 시작합니다.
event_system_manager = EventSystemManager()
event_system_manager.start()  # 이벤트 시스템 시작


def ensure_mouse_clicked_by_coordination_history(key_name: str, func_n, history_reset: bool = False) -> tuple[int, int]:
    if history_reset:
        logging.debug(f"마우스 좌표 기록 초기화 요청: {key_name}, {func_n}")
        ensure_mouse_coordination_history_reset(key_name=key_name, func_n=func_n)

    file_id = get_env_var_id(key_name, func_n)
    history_dir = D_TASK_ORCHESTRATOR_CLI_SENSITIVE / "mouse_click_history"
    history_dir.mkdir(parents=True, exist_ok=True)
    history_file = history_dir / f"{file_id}.txt"

    if history_file.exists():
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                coords_str = f.read().strip()
            x_str, y_str = coords_str.split(',')
            x, y = int(x_str), int(y_str)

            logging.debug(f"마우스 좌표 기록 발견: ({x}, {y}). 해당 위치를 클릭합니다.")
            mouse_controller = mouse.Controller()
            mouse_controller.position = (x, y)
            ensure_mouse_moved(x, y, duration=0.5)
            mouse_controller.click(mouse.Button.left, 1)
            logging.debug(f"마우스 클릭 완료: ({x}, {y})")
            event_system_manager.event_queue.add_event(create_event(EventType.CLICK_DETECTED_EVENT, {'key_name': key_name, 'func_n': func_n}, source='ensure_mouse_clicked_by_coordination_history'))
            return (x, y)  # Return coordinates here

        except Exception as e:
            logging.error(f"마우스 좌표 파일 읽기 또는 클릭 중 오류 발생: {e}. 새 좌표를 기록합니다.")
            return _record_mouse_click(key_name, func_n, history_file)
    else:
        logging.debug(f"마우스 좌표 기록이 없습니다. 새 좌표를 기록합니다.")
        return _record_mouse_click(key_name, func_n, history_file)


def _record_mouse_click(key_name, func_n, history_file: Path) -> tuple[int, int]:  # Changed return type to non-None
    while True:  # Loop until a valid click is recorded
        logging.debug(f"{key_name} 진행을 위해, 클릭해주세요")
        ensure_spoken(f"{key_name} 진행을 위해, 클릭해주세요")
        clicked_coords = None

        def on_click(x, y, button, pressed):
            nonlocal clicked_coords
            if pressed:
                clicked_coords = (x, y)
                logging.debug(f"마우스 클릭 감지: ({x}, {y})")
                return False  # Stop listener

        with mouse.Listener(on_click=on_click) as listener:
            listener.join()

        if clicked_coords:
            x, y = clicked_coords
            try:
                with open(history_file, 'w', encoding='utf-8') as f:
                    f.write(f"{x},{y}")
                logging.debug(f"마우스 좌표 저장 완료: ({x}, {y}) -> {history_file}")
                event_system_manager.event_queue.add_event(create_event(EventType.CLICK_DETECTED_EVENT, {'key_name': key_name, 'func_n': func_n}, source='_record_mouse_click'))
                return (x, y)  # Always return recorded coordinates here
            except Exception as e:
                logging.error(f"마우스 좌표 저장 중 오류 발생: {e}. 다시 시도합니다.")
                # Loop will continue
        else:
            logging.warning("마우스 클릭이 감지되지 않았습니다. 다시 시도합니다.")
            # Loop will continue
