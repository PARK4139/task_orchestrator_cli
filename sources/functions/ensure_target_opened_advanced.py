
import logging
from pathlib import Path

def ensure_target_opened_advanced(target_path: str):
    """
    주어진 타겟 경로가 URL, 파일, 디렉토리인지 판단하여 적절한 방식으로 엽니다.
    - URL인 경우: ensure_url_opened()를 사용하여 엽니다.
    - 파일 또는 디렉토리인 경우: ensure_pnx_opened_by_ext()를 사용하여 엽니다.
    """
    # lazy imports
    from sources.functions.ensure_task_orchestrator_cli_log_initialized import ensure_task_orchestrator_cli_log_initialized
    from sources.functions.ensure_url_opened import ensure_url_opened
    from sources.functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext

    ensure_task_orchestrator_cli_log_initialized(__file__)

    if not isinstance(target_path, str) or not target_path:
        logging.error("유효하지 않은 타겟 경로가 입력되었습니다.")
        return

    # URL Check
    if target_path.startswith('http://') or target_path.startswith('https://'):
        logging.debug(f"타겟 '{target_path}'는 URL로 분류되었습니다. 'ensure_url_opened'로 엽니다.")
        ensure_url_opened(target_path)
        return

    # File/Directory Check
    p = Path(target_path)
    if p.exists():
        if p.is_dir():
            classification = "디렉토리"
        else:
            classification = "파일"
        
        logging.debug(f"타겟 '{target_path}'는 {classification}(으)로 분류되었습니다. 'ensure_pnx_opened_by_ext'로 엽니다.")
        ensure_pnx_opened_by_ext(target_path)
    else:
        logging.error(f"타겟 '{target_path}'는 존재하지 않는 파일 또는 디렉토리입니다.")

if __name__ == '__main__':
    # 테스트 케이스
    test_url = "https://github.com"
    test_file = __file__ # 현재 파일
    test_dir = str(Path(__file__).parent) # 현재 디렉토리
    test_invalid_path = "C:/invalid/path/that/does/not/exist.txt"

    print(f"--- 테스트: URL ---")
    ensure_target_opened_advanced(test_url)

    print(f"\n--- 테스트: 파일 ---")
    ensure_target_opened_advanced(test_file)

    print(f"\n--- 테스트: 디렉토리 ---")
    ensure_target_opened_advanced(test_dir)

    print(f"\n--- 테스트: 유효하지 않은 경로 ---")
    ensure_target_opened_advanced(test_invalid_path)
