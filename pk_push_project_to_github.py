import inspect
import os
import re
import subprocess
import sys
import time
from pathlib import Path

from colorama import init as pk_colorma_init

pk_colorma_init(autoreset=True)

# 기본 상수
SCRIPT_NAME = Path(__file__).name
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
DIVIDER = "_______________________________________"

# 전역 스텝 카운터
step_counter = 0


def print_status(step_num: int, cmd: str, code: int, output: str) -> str:
    if code == 0:
        label, color = "SUCCESS", GREEN
    elif "nothing to commit" in output.lower():
        label, color = "SKIPPED", YELLOW
    elif "everything up-to-date" in output.lower():
        label, color = "SKIPPED", YELLOW
    else:
        label, color = "FAILED", RED

    print(f"[ {color}{label}{RESET} ] [{step_num}] {cmd}")
    return label


def run_command(cmd: str, capture_output=False):
    try:
        if capture_output:
            result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
            return result.returncode, result.stdout + result.stderr
        else:
            result = subprocess.run(cmd, shell=True)
            return result.returncode, ""
    except Exception as e:
        return 1, str(e)


def get_next_commit_number():
    code, log_output = run_command('git log -n 20 --pretty=format:%s', capture_output=True)
    if code != 0:
        return 1
    numbers = []
    for line in log_output.splitlines():
        match = re.match(r"\[(\d+)\]", line)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def fail_and_exit(start_time):
    print(f"\n{RED}[!] Aborting further steps. Current git status:{RESET}")
    _, status_out = run_command("git status", capture_output=True)
    print(status_out.strip())
    duration = time.time() - start_time
    print(f"{RED}process failed at {time.strftime('%Y-%m-%d %H:%M:%S')} (elapsed {duration:.2f} sec){RESET}")
    sys.exit(1)


def get_history_file_path(file_id: str) -> Path:
    history_dir = Path.home() / ".git_config_history"
    history_dir.mkdir(parents=True, exist_ok=True)
    return history_dir / f"history_{file_id}.txt"


def get_text_from_history_file(file_id: str) -> str | None:
    file_path = get_history_file_path(file_id)
    if not file_path.exists():
        file_path.write_text("")  # create an empty file
        return None
    content = file_path.read_text().strip()
    return content if content else None


def set_text_from_history_file(file_id: str, text: str):
    """Save text to the corresponding history file."""
    file_path = get_history_file_path(file_id)
    file_path.write_text(text.strip())


def ensure_git_project_pushed():
    func_n = inspect.currentframe().f_code.co_name

    global step_counter
    start_time = time.time()
    print(DIVIDER)
    print(f"LOCAL LEPO : {GREEN}{os.getcwd()}{RESET}")
    print(f"STARTED AT : {GREEN}{time.strftime('%Y-%m-%d %H:%M:%S')}{RESET}")

    # 0. git config set
    user_email = get_text_from_history_file("user_email") or ""
    user_name = get_text_from_history_file("user_name") or ""

    if len(user_email.strip()) == 0:
        user_email = input("user_email=").strip()
        cmd = f'git config --global user.email "{user_email}"'
        code, output = run_command(cmd, capture_output=True)
        print(output.strip())
        set_text_from_history_file("user_email", user_email)
        status = print_status(step_counter + 1, cmd, code, output)
        if status == "FAILED":
            fail_and_exit(start_time)
        step_counter += 1

    if len(user_name.strip()) == 0:
        user_name = input("user_name=").strip()
        cmd = f'git config --global user.name "{user_name}"'
        code, output = run_command(cmd, capture_output=True)
        print(output.strip())
        set_text_from_history_file("user_name", user_name)
        status = print_status(step_counter + 1, cmd, code, output)
        if status == "FAILED":
            fail_and_exit(start_time)
        step_counter += 1

    # 1. git add
    print(DIVIDER)
    cmd = "git add ."
    code, output = run_command(cmd, capture_output=True)
    print(output.strip())
    status = print_status(step_counter + 1, cmd, code, output)
    if status == "FAILED":
        fail_and_exit(start_time)
    step_counter += 1

    # 2. git commit
    print(DIVIDER)
    commit_number = get_next_commit_number()
    commit_message = None
    key_name = "commit_message"
    try:
        from pkg_py.functions_split.get_file_id import get_file_id
        from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
        from pkg_py.functions_split.get_time_as_ import get_time_as_
        from pkg_py.functions_split.get_value_completed import get_value_completed
        from pkg_py.pk_system_object.PkMessages2025 import PkMessages2025
        option_values = [PkMessages2025.EMERGENCY_BACKUP, "add: ", "fix: ", "refactor: ", "found: problem", "chore: various improvements and updates across multiple files", "refactor: restructure and update multiple files with improved messages and translations"]
        commit_message = get_value_completed(key_hint='commit_message=', values=option_values)
        commit_message = commit_message.strip()
        if commit_message == PkMessages2025.EMERGENCY_BACKUP or "":
            commit_message = f"feat: auto pushed (made savepoint) by {SCRIPT_NAME} at {get_time_as_("%Y-%m-%d %H:%M")}"
    except:
        commit_message = input("commit_message=").strip()
        if commit_message == "":
            commit_message = f"feat: auto pushed (made savepoint) by {SCRIPT_NAME}"

    cmd = f'git commit -m "{commit_message}"'
    code, output = run_command(cmd, capture_output=True)
    print(output.strip())
    status = print_status(step_counter + 1, cmd, code, output)
    if status == "FAILED":
        fail_and_exit(start_time)
    step_counter += 1

    # 3. git push
    print(DIVIDER)
    cmd = "git push"
    code, output = run_command(cmd, capture_output=True)
    print(output.strip())
    status = print_status(step_counter + 1, cmd, code, output)
    if status == "FAILED":
        fail_and_exit(start_time)
    step_counter += 1

    print(DIVIDER)
    if any(protocol in output for protocol in ["To https://", "To http://", "To git@"]):
        pass
    elif "everything up-to-date" in output.lower():
        pass
    else:
        fail_and_exit(start_time)

    duration = time.time() - start_time
    print(f"{GREEN}ALL PROCESS COMPLETED SUCCESSFULLY. TOTAL EXECUTION TIME: {duration:.2f} SECONDS {RESET}")


if __name__ == "__main__":
    ensure_git_project_pushed()