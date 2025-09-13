from pathlib import Path
import logging
import os

# Lazy import for get_env_var_id
try:
    from functions.get_env_var_name_id import get_env_var_id
except ImportError:
    def get_env_var_id(key_name, func_n):
        return f"{key_name.upper()}_{func_n.upper()}"

# Lazy import for D_TASK_ORCHESTRATOR_CLI_SENSITIVE
try:
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
except ImportError:
    D_TASK_ORCHESTRATOR_CLI_SENSITIVE = Path(os.path.expanduser("~")) / "Downloads" / "task_orchestrator_cli" / "task_orchestrator_cli_sensitive"


def ensure_slept_by_following_history_reset(key_name: str, func_n: str) -> bool:
    """
    주어진 key_name과 func_n에 해당하는 대기 시간 기록 파일을 삭제합니다.
    """
    file_id = f"{get_env_var_id(key_name, func_n)}_for_ensure_slept" # Modified file_id
    history_dir = D_TASK_ORCHESTRATOR_CLI_SENSITIVE / "sleep_duration_history" # Modified directory
    history_file = history_dir / f"{file_id}.txt"

    if history_file.exists():
        try:
            history_file.unlink()  # Delete the file
            logging.debug(f"대기 시간 기록 파일이 성공적으로 삭제되었습니다: {history_file}")
            return True
        except Exception as e:
            logging.error(f"마우스 좌표 기록 파일 삭제 중 오류 발생: {e}")
            return False
    else:
        logging.debug(f"대기 시간 기록 파일이 존재하지 않습니다: {history_file}")
        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    # Example usage for testing
    test_key = "TEST_RESET_SLEEP"
    test_func_n = "FUNC_RESET_SLEEP"

    # Create a dummy file for testing deletion
    dummy_dir = D_TASK_ORCHESTRATOR_CLI_SENSITIVE / "sleep_duration_history"
    dummy_dir.mkdir(parents=True, exist_ok=True)
    dummy_file = dummy_dir / f"{get_env_var_id(test_key, test_func_n)}_for_ensure_slept.txt"
    with open(dummy_file, 'w') as f:
        f.write("5.0")
    logging.debug(f"더미 파일 생성: {dummy_file}")

    # Test case 1: Delete an existing file
    logging.debug("\n--- 테스트 1: 기존 파일 삭제 ---")
    ensure_slept_by_following_history_reset(test_key, test_func_n)

    # Test case 2: Try to delete a non-existent file
    logging.debug("\n--- 테스트 2: 존재하지 않는 파일 삭제 시도 ---")
    ensure_slept_by_following_history_reset("NON_EXISTENT_SLEEP", "FILE_SLEEP")
