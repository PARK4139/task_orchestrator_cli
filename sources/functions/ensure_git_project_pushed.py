import traceback

from functions.ensure_console_paused import ensure_console_paused
from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
from functions.ensure_windows_killed_like_human import ensure_windows_killed_like_human
from functions.get_easy_speakable_text import get_easy_speakable_text
from functions.get_text_cyan import get_text_cyan
from functions.get_text_yellow import get_text_yellow

step_counter = 1


def _ensure_git_add(start_time):
    import logging
    from sources.functions.ensure_status_printed_step import ensure_status_printed_step
    from sources.functions.run_command import run_command
    cmd = "git add ."
    code, output = run_command(cmd, capture_output=True)
    outputs = output.split('\n')
    for _ in outputs:
        logging.debug(f"{_}")
    label = ensure_status_printed_step(step_counter + 1, cmd, code, output)
    if not ensure_label_process_done(label, start_time):
        return


def get_auto_commit_message(__file__):
    from functions import get_time_as_
    from functions.get_nx import get_nx
    auto_commit_message = f"feat: make savepoint, automatically by {get_nx(__file__)} at {get_time_as_("%Y-%m-%d %H:%M")}"
    return auto_commit_message


def _ensure_auto_commit_message_used(__file__):
    from functions.ensure_spoken import ensure_spoken

    commit_message = get_auto_commit_message(__file__)
    # ensure_spoken("오토 커밋 메시지가 사용되었습니다")
    return commit_message


def _ensure_git_commit(start_time, with_commit_massage, __file__, editable):
    from functions.ensure_status_printed_step import ensure_status_printed_step
    from functions.run_command import run_command
    from objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP
    from objects.pk_etc import PK_UNDERLINE
    from sources.functions.ensure_value_completed_advanced import ensure_value_completed_advanced

    import logging
    from sources.objects.pk_local_test_activate import LTA

    logging.debug(f'''with_commit_massage={with_commit_massage} {'%%%FOO%%%' if LTA else ''}''')

    if with_commit_massage == False:
        commit_message = _ensure_auto_commit_message_used(__file__)
    else:
        try:
            key_name = 'commit_message'
            from functions.get_caller_n import get_caller_n
            func_n = get_caller_n()

            auto_make_save_mode = "<<<<<< 치트키 : 오토 커밋메시지로 푸쉬 >>>>>>"
            value = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=[auto_make_save_mode], editable=editable)
            logging.debug(f'''fzf로부터 받은 값: {value} {'%%%FOO%%%' if LTA else ''}''')
            value = value or ""
            if value == auto_make_save_mode:
                logging.debug(f'''commit_message is empty''')
                commit_message = _ensure_auto_commit_message_used(__file__)
            else:
                commit_message = value
            logging.debug(f'''finally checked commit_message: {get_text_cyan(commit_message)} {'%%%FOO%%%' if LTA else ''}''')
        except Exception as e:
            # fzf 실행 실패 시 자동으로 기본 메시지 사용 (중복 입력 방지)
            import traceback
            logging.debug(f"{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RED']}{PK_UNDERLINE}")
            logging.debug(f"FZF 실행 실패 - 상세 오류 정보{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']}")
            logging.debug(f'''예외 타입: {type(e).__name__} {'%%%FOO%%%' if LTA else ''}''')
            logging.debug(f'''예외 메시지: {str(e)} {'%%%FOO%%%' if LTA else ''}''')
            logging.debug(f'''상세 스택 트레이스: {'%%%FOO%%%' if LTA else ''}''')
            logging.debug(f"{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RED']}{PK_UNDERLINE}")
            logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
            logging.debug(f"{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['YELLOW']}{PK_UNDERLINE}")
            logging.debug(f"[SOLUTION] 해결 방법:{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']}")
            logging.debug(f"1. Windows: choco install fzf 또는 scoop install fzf")
            logging.debug(f"2. Linux: sudo apt install fzf 또는 sudo yum install fzf")
            logging.debug(f"3. fzf가 PATH에 있는지 확인: which fzf 또는 where fzf")
            logging.debug(f"{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['YELLOW']}{PK_UNDERLINE}" + TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET'])
            logging.debug(f'''[FALLBACK] 기본 커밋 메시지를 사용합니다 {'%%%FOO%%%' if LTA else ''}''')
            commit_message = f"msp"
            logging.debug(f'''[FALLBACK] commit_message={get_text_yellow(commit_message)} {'%%%FOO%%%' if LTA else ''}''')

    cmd = f'git commit -m "{commit_message}"'
    code, output = run_command(cmd, capture_output=True)
    outputs = output.strip().split('\n')
    for _ in outputs:
        logging.debug(f"{_}")
    label = ensure_status_printed_step(step_counter + 1, cmd, code, output)
    if not ensure_label_process_done(label, start_time):
        return


def _ensure_upstream_branch_checked(current_branch):
    import logging
    from sources.functions.run_command import run_command
    cmd_upstream = f"git rev-parse --abbrev-ref {current_branch}@{{upstream}}"
    code_upstream, output_upstream = run_command(cmd_upstream, capture_output=True)
    cmd = None
    if code_upstream != 0:
        logging.debug(f"업스트림 브랜치가 설정되지 않음. 설정 중...")
        # 업스트림 설정과 함께 푸시
        cmd = f"git push --set-upstream origin {current_branch}"
    else:
        upstream_branch = output_upstream.strip()
        logging.debug(f"업스트림 브랜치: {upstream_branch}")

        # 3-4. 로컬과 원격 브랜치 비교
        cmd_ahead_behind = f"git rev-list --left-right --count origin/{current_branch}...{current_branch}"
        code_ahead_behind, output_ahead_behind = run_command(cmd_ahead_behind, capture_output=True)

        return cmd, code_ahead_behind, output_ahead_behind


def _ensure_git_pushed(cmd, code_ahead_behind, output_ahead_behind, current_branch, start_time):
    from sources.functions.ensure_git_state_checked import ensure_git_state_checked
    from sources.functions.ensure_status_printed_step import ensure_status_printed_step

    import logging
    from sources.functions.run_command import run_command
    if code_ahead_behind == 0:
        behind, ahead = output_ahead_behind.strip().split('\t')
        logging.debug(f"브랜치 상태 - 뒤처진 커밋: {behind}개, 앞선 커밋: {ahead}개")
        if int(behind) > 0:
            logging.debug(f"로컬 브랜치가 {behind}개 커밋만큼 뒤처져 있습니다.")
            logging.debug("강제 푸시를 시도합니다...")
            cmd = f"git push origin {current_branch} --force-with-lease"
        else:
            cmd = "git push"
    else:
        # 원격 브랜치 정보를 가져올 수 없는 경우
        logging.debug("원격 브랜치 정보를 확인할 수 없습니다. 일반 푸시를 시도합니다.")
        cmd = "git push"
    logging.debug(f"cmd={cmd}")
    state_code, output = run_command(cmd, capture_output=True)
    outputs = output.strip().split('\n')
    for _ in outputs:
        logging.debug(f"{_}")

    # 푸시 실패 시 추가 시도
    if state_code != 0:
        if "no upstream branch" in output.lower():
            logging.debug("업스트림 브랜치 미설정으로 인한 실패. 재시도...")
            cmd_retry = f"git push --set-upstream origin {current_branch}"
            logging.debug(f"cmd_retry={cmd_retry}")
            state_code, output = run_command(cmd_retry, capture_output=True)
            outputs = output.strip().split('\n')
            for _ in outputs:
                logging.debug(f"{_}")

        elif "non-fast-forward" in output.lower() or "rejected" in output.lower():
            logging.debug("Fast-forward 불가로 인한 실패. 강제 푸시 시도...")
            cmd_force = f"git push origin {current_branch} --force-with-lease"
            logging.debug(f"cmd_force={cmd_force}")
            state_code, output = run_command(cmd_force, capture_output=True)
            outputs = output.strip().split('\n')
            for _ in outputs:
                logging.debug(f"{_}")

            if state_code != 0:
                logging.debug("--force-with-lease 실패. 완전 강제 푸시 시도...")
                cmd_force_hard = f"git push origin {current_branch} --force"
                logging.debug(f"cmd_force_hard={cmd_force_hard}")
                state_code, output = run_command(cmd_force_hard, capture_output=True)
                outputs = output.strip().split('\n')
                for _ in outputs:
                    logging.debug(f"{_}")

    label = ensure_status_printed_step(step_counter + 1, cmd, state_code, output)
    if label == "FAILED":
        logging.debug("푸시 실패 상세 분석 ===")
        logging.debug(f"최종 명령어: {cmd}")
        logging.debug(f"반환 코드: {state_code}")
        logging.debug(f"출력 메시지: {output}")
        logging.debug("가능한 해결 방법 ===")
        logging.debug("1. git pull origin main (원격 변경사항 병합)")
        logging.debug("2. git push --force (강제 푸시)")
        logging.debug("3. GitHub 인증 토큰 확인")
        logging.debug("4. 네트워크 연결 상태 확인")
        state = ensure_git_state_checked(start_time, label)
        if state == False:
            return
    return state_code, output


def ensure_label_process_done(label, start_time):
    from functions.ensure_git_state_checked import ensure_git_state_checked
    if label == "FAILED":
        state = ensure_git_state_checked(start_time, label)
        if state == False:
            return False

    if label == "SKIPPED":
        state = ensure_git_state_checked(start_time, label)
        if state == False:
            return False
    return True


def ensure_git_project_pushed(d_local_repo, with_commit_massage=None):
    from functions.ensure_spoken import ensure_spoken
    from functions.get_nx import get_nx

    import os
    import time

    import logging
    from sources.functions.ensure_git_state_checked import ensure_git_state_checked
    from sources.functions.get_text_from_history_file import get_text_from_history_file
    from sources.functions.ensure_status_printed_step import ensure_status_printed_step
    from sources.functions.run_command import run_command
    from sources.functions.set_text_from_history_file import set_text_from_history_file
    from sources.objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP
    from sources.objects.pk_etc import PK_UNDERLINE
    from sources.objects.pk_local_test_activate import LTA

    pwd = os.getcwd()

    try:

        ensure_windows_killed_like_human(window_title=rf"pk_ensure_routine_file_executed_as_hot_reloader.py")

        os.chdir(d_local_repo)

        global step_counter

        if LTA:
            # pk_option
            # if with_commit_massage is None:
            # with_commit_massage = False
            # editable = True

            # pk_option
            if with_commit_massage is None:
                with_commit_massage = True
            editable = False
        else:
            if with_commit_massage is None:
                with_commit_massage = True
            editable = False

        start_time = time.time()
        logging.debug(PK_UNDERLINE)
        d_project_to_push = get_nx(os.getcwd())
        # easy_speakable_text = get_easy_speakable_text(d_project_to_push)
        # ensure_spoken(rf"{easy_speakable_text} 푸쉬 시도")
        logging.debug(f"LOCAL LEPO : {TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['CYAN']}{d_project_to_push}{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']}")
        logging.debug(f"STARTED AT : {TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['CYAN']}{time.strftime('%Y-%m-%d %H:%M:%S')}{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']}")

        # git config set
        user_email = get_text_from_history_file("user_email") or ""
        user_name = get_text_from_history_file("user_name") or ""

        if len(user_email.strip()) == 0:
            user_email = input("user_email=").strip()
            cmd = f'git config --global user.email "{user_email}"'
            code, output = run_command(cmd, capture_output=True)
            logging.debug(output.strip())
            set_text_from_history_file("user_email", user_email)
            label = ensure_status_printed_step(step_counter + 1, cmd, code, output)
            if not ensure_label_process_done(label, start_time):
                ensure_console_paused()
            step_counter += 1

        if len(user_name.strip()) == 0:
            user_name = input("user_name=").strip()
            cmd = f'git config --global user.name "{user_name}"'
            code, output = run_command(cmd, capture_output=True)
            logging.debug(output.strip())
            set_text_from_history_file("user_name", user_name)
            label = ensure_status_printed_step(step_counter + 1, cmd, code, output)
            if not ensure_label_process_done(label, start_time):
                ensure_console_paused()
            step_counter += 1

        # git add
        logging.debug(PK_UNDERLINE)
        _ensure_git_add(start_time)
        step_counter += 1

        # git commit
        logging.debug(PK_UNDERLINE)
        _ensure_git_commit(start_time, with_commit_massage, __file__, editable)
        # commit_number = get_next_commit_number()
        step_counter += 1

        # git push (에러 처리 강화)
        logging.debug(PK_UNDERLINE)

        # 현재 브랜치 확인 (에러 처리 강화)
        cmd_branch = "git branch --show-current"
        code_branch, output_branch = run_command(cmd_branch, capture_output=True)
        current_branch = output_branch.strip()
        logging.debug(f"현재 브랜치: {current_branch}")

        # 원격 저장소 확인 (에러 처리 강화)
        cmd_remote = "git remote -v"
        code_remote, output_remote = run_command(cmd_remote, capture_output=True)
        outputs = output_remote.split("\n")
        for output in outputs:
            logging.debug(f"원격 저장소: {output}")

        # 업스트림 브랜치 확인 (에러 처리 강화)
        cmd, code_ahead_behind, output_ahead_behind = _ensure_upstream_branch_checked(current_branch)

        # 실제 푸시 실행
        code, output = _ensure_git_pushed(cmd, code_ahead_behind, output_ahead_behind, current_branch, start_time)
        step_counter += 1

        logging.debug(PK_UNDERLINE)
        if any(protocol in output for protocol in ["To https://", "To http://", "To git@"]):
            pass
        elif "everything up-to-date" in output.lower():
            pass # TODO
        else:
            label = "FAILED"
            if ensure_git_state_checked(start_time, label) == False:
                ensure_console_paused()

        duration = time.time() - start_time
        logging.debug(f"{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['CYAN']}ALL PROCESS COMPLETED SUCCESSFULLY. TOTAL EXECUTION TIME: {duration:.2f} SECONDS {TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']}")

        return {
            "state": True
        }
    except:
        ensure_debug_loged_verbose(traceback=traceback)
    finally:
        os.chdir(pwd)
