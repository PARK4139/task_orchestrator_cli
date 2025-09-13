import logging
import time
from pathlib import Path
import importlib.util
from pynput import mouse, keyboard

# GEMINI.md 규칙에 따라 lazy import를 함수 내부에 배치합니다.

def ensure_routine_macro_code_return(key_name, func_n, history_reset=False):
    """
    마우스/키보드/시간을 측정하여 매크로 코드를 작성 또는 기존 매크로를 실행합니다.
    - key_name, func_n을 조합하여 파일 ID를 생성하고 파일을 관리합니다.
    - 기존 파일이 있으면 해당 매크로 코드를 실행합니다.
    - 파일이 없거나 history_reset=True이면 마우스/키보드/시간을 측정하여 매크로 코드를 파일에 작성합니다.
    - 작성이 완료되면 ensure_target_opened_advanced를 호출하여 생성된 파일을 엽니다.
    """
    # lazy imports for project-specific modules
    try:
        from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
        from sources.functions.ensure_target_opened_advanced import ensure_target_opened_advanced
        from sources.functions.ensure_spoken import ensure_spoken
        # The executed macro code will need these, so we ensure they are available.
        # We don't call them directly in this function, but they need to be in the scope
        # for the exec() call.
        from sources.functions.ensure_typed import ensure_typed
        from sources.functions.ensure_pressed import ensure_pressed
        from sources.functions.ensure_clicked import ensure_clicked
    except ImportError as e:
        logging.error(f"Failed to import necessary modules: {e}")
        return

    d_routine_macros = Path(D_TASK_ORCHESTRATOR_CLI_SENSITIVE) / "routine_macros"
    d_routine_macros.mkdir(exist_ok=True)

    file_id = f"routine_macro_{key_name}_{func_n}.py"
    macro_file_path = d_routine_macros / file_id

    should_record = history_reset or not macro_file_path.exists()

    if should_record:
        logging.info(f"Recording new macro to: {macro_file_path}. Press 'Esc' to stop.")
        ensure_spoken(text="매크로 녹화를 시작합니다. 종료하려면 Esc 키를 누르세요.")

        events = []
        last_time = time.time()

        def add_event(event_type, **kwargs):
            nonlocal last_time
            current_time = time.time()
            delay = (current_time - last_time) * 1000  # milliseconds
            if delay > 100: # 최소 100ms 이상일 때만 시간 기록
                events.append(f"ensure_spoken(miliseconds={int(delay)})")
            
            if event_type == 'click':
                events.append(f"ensure_clicked({kwargs['x']}, {kwargs['y']})")
            elif event_type == 'press':
                # pynput.keyboard.Key.xxx -> "xxx"
                key_repr = repr(kwargs['key']).replace("Key.", "").replace("'", "")
                events.append(f"ensure_pressed('{key_repr}')")

            last_time = current_time

        def on_click(x, y, button, pressed):
            if pressed:
                add_event('click', x=x, y=y)

        def on_press(key):
            if key == keyboard.Key.esc:
                return False  # Stop listener
            add_event('press', key=key)
        
        # pynput은 타이핑을 직접 캡처하기 어렵습니다.
        # 키 입력을 조합하여 타이핑을 추정하는 대신, `ensure_pressed`로 각 키를 기록합니다.
        # 사용자가 `ensure_typed`를 원하면 수동으로 수정해야 합니다.

        listener_mouse = mouse.Listener(on_click=on_click)
        listener_keyboard = keyboard.Listener(on_press=on_press)

        listener_mouse.start()
        listener_keyboard.start()
        
        listener_keyboard.join() # Wait until 'Esc' is pressed
        listener_mouse.stop()

        if events:
            # Add necessary imports to the beginning of the macro file
            header = '''from sources.functions.ensure_spoken import ensure_spoken
from sources.functions.ensure_typed import ensure_typed
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_clicked import ensure_clicked

'''
            macro_code = header + "\n".join(events)
            
            with open(macro_file_path, "w", encoding="utf-8") as f:
                f.write(macro_code)
            
            logging.info(f"Macro recording finished. Saved to {macro_file_path}")
            ensure_spoken(text="매크로 녹화가 완료되었습니다.")
            
            # Open the created file for user to verify
            ensure_target_opened_advanced(str(macro_file_path))
        else:
            logging.warning("No events were recorded.")
            ensure_spoken(text="기록된 매크로 이벤트가 없습니다.")

    else:
        logging.info(f"Executing existing macro: {macro_file_path}")
        ensure_spoken(text=f"{key_name} {func_n} 매크로를 실행합니다.")
        try:
            spec = importlib.util.spec_from_file_location(macro_file_path.stem, macro_file_path)
            macro_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(macro_module)
            logging.info("Macro execution completed.")
            ensure_spoken(text="매크로 실행이 완료되었습니다.")
        except Exception as e:
            logging.error(f"Failed to execute macro {macro_file_path}: {e}")
            ensure_spoken(text="매크로 실행 중 오류가 발생했습니다.")

if __name__ == '__main__':
    # 사용 예시 (직접 실행하여 테스트)
    # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # 처음 실행 시 녹화, 두 번째 실행 시 재생
    # ensure_routine_macro_code_return("test_key", "test_func")
    
    # 강제 재녹화
    # ensure_routine_macro_code_return("test_key", "test_func", history_reset=True)
    pass
