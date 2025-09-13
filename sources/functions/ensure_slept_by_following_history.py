from pathlib import Path
import logging
import os
import time

# Lazy imports (similar to ensure_mouse_clicked_by_coordination_history)
try:
    from functions.get_env_var_name_id import get_env_var_id
except ImportError:
    def get_env_var_id(key_name, func_n):
        return f"{key_name.upper()}_{func_n.upper()}"

try:
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
except ImportError:
    D_TASK_ORCHESTRATOR_CLI_SENSITIVE = Path(os.path.expanduser("~")) / "Downloads" / "task_orchestrator_cli" / "task_orchestrator_cli_sensitive"

try:
    from functions.ensure_slept_by_following_history_reset import ensure_slept_by_following_history_reset
except ImportError:
    # Fallback for reset function if not yet created
    def ensure_slept_by_following_history_reset(key_name: str, func_n: str) -> bool:
        logging.warning("ensure_slept_by_following_history_reset 함수가 아직 구현되지 않았습니다.")
        return False

from sources.objects.pk_event_system import EventSystemManager, EventType, create_event

# 전역 이벤트 시스템 인스턴스 (ensure_mouse_clicked_by_coordination_history.py와 동일한 인스턴스 사용)
event_system_manager = EventSystemManager()
event_system_manager.start() # 이벤트 시스템 시작 (이미 시작되었을 수 있으나, 중복 호출은 무시됨)


def ensure_slept_by_following_history(key_name: str, func_n: str, history_reset: bool = False) -> float | None:
    """
    이전 기록에 따라 지정된 시간만큼 대기하거나, 기록이 없으면 사용자 입력을 받아 대기 시간을 기록합니다.
    """
    if history_reset:
        logging.debug(f"대기 시간 기록 초기화 요청: {key_name}, {func_n}")
        ensure_slept_by_following_history_reset(key_name=key_name, func_n=func_n)

    file_id = f"{get_env_var_id(key_name, func_n)}_for_ensure_slept"
    history_dir = D_TASK_ORCHESTRATOR_CLI_SENSITIVE / "sleep_duration_history"
    history_dir.mkdir(parents=True, exist_ok=True)
    history_file = history_dir / f"{file_id}.txt"

    if history_file.exists():
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                duration_str = f.read().strip()
            duration = float(duration_str)
            
            logging.debug(f"대기 시간 기록 발견: {duration}초. 해당 시간만큼 대기합니다.")
            time.sleep(duration)
            logging.debug(f"대기 완료: {duration}초")
            return duration
            
        except Exception as e:
            logging.error(f"대기 시간 파일 읽기 또는 대기 중 오류 발생: {e}. 새 시간을 기록합니다.")
            return _measure_and_record_duration(key_name, func_n, history_file)
    else:
        logging.debug(f"대기 시간 기록이 없습니다. 새 시간을 기록합니다.")
        return _measure_and_record_duration(key_name, func_n, history_file)

def _measure_and_record_duration(key_name: str, func_n: str, history_file: Path) -> float | None:
    logging.debug(f"대기 시간 측정을 시작합니다. 마우스 클릭, 키보드 입력 또는 이벤트 발생 시 측정이 종료됩니다. (key_name: {key_name}, func_n: {func_n})")
    
    import threading
    from pynput import mouse, keyboard

    stop_event = threading.Event()
    start_time = time.time()

    # Event system handler
    def click_event_handler(event):
        # 이벤트 데이터에 key_name과 func_n이 포함되어 있는지 확인하고 필터링
        if event.data.get('key_name') == key_name and event.data.get('func_n') == func_n:
            logging.debug(f"이벤트 감지: {event.type.value}. 측정 종료. (key_name: {key_name}, func_n: {func_n})")
            stop_event.set()

    # Register the event handler
    event_system_manager.event_queue.register_handler(EventType.CLICK_DETECTED_EVENT, click_event_handler)

    def on_click(x, y, button, pressed):
        if pressed:
            logging.debug(f"마우스 클릭 감지: ({x}, {y}). 측정 종료.")
            stop_event.set()
            return False  # Stop mouse listener

    def on_press(key):
        try:
            logging.debug(f"키보드 입력 감지: {key}. 측정 종료.")
        except AttributeError:
            logging.debug(f"특수 키 입력 감지: {key}. 측정 종료.")
        stop_event.set()
        return False  # Stop keyboard listener

    mouse_listener = mouse.Listener(on_click=on_click)
    keyboard_listener = keyboard.Listener(on_press=on_press)

    mouse_listener.start()
    keyboard_listener.start()

    stop_event.wait() # Wait until an event is set

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Ensure listeners are stopped and joined
    if mouse_listener.running:
        mouse_listener.stop()
    if keyboard_listener.running:
        keyboard_listener.stop()
    
    # Unregister the event handler
    event_system_manager.event_queue.unregister_handler(EventType.CLICK_DETECTED_EVENT, click_event_handler)

    # Give a moment for threads to finish stopping
    time.sleep(0.1)

    logging.debug(f"측정된 대기 시간: {elapsed_time:.2f}초")

    try:
        with open(history_file, 'w', encoding='utf-8') as f:
            f.write(f"{elapsed_time}")
        logging.debug(f"대기 시간 저장 완료: {elapsed_time:.2f}초 -> {history_file}")
        return elapsed_time
    except Exception as e:
        logging.error(f"대기 시간 저장 중 오류 발생: {e}")
        return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Example usage for testing
    
    # Test case 1: Record a duration
    logging.debug("\n--- 테스트 1: 새 대기 시간 기록 ---")
    ensure_slept_by_following_history("TEST_SLEEP", "FUNC_X")
    
    # Test case 2: Replay the duration
    logging.debug("\n--- 테스트 2: 기록된 대기 시간 재생 ---")
    ensure_slept_by_following_history("TEST_SLEEP", "FUNC_X")
    
    # Test case 3: Record another duration (different key)
    logging.debug("\n--- 테스트 3: 다른 키로 새 대기 시간 기록 ---")
    ensure_slept_by_following_history("ANOTHER_SLEEP", "FUNC_Y")
    
    # Test case 4: Reset and record again
    logging.debug("\n--- 테스트 4: 리셋 후 다시 기록 ---")
    ensure_slept_by_following_history("TEST_SLEEP", "FUNC_X", history_reset=True)
    ensure_slept_by_following_history("TEST_SLEEP", "FUNC_X")
