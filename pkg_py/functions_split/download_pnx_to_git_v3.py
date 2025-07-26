import yt_dlp
import re

from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.directories_reuseable import D_PROJECT

from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def download_pnx_to_git_v3(d_working, git_repo_url, commit_msg, branch_n):
    import traceback
    import threading
    import time
    # from colorama import init as pk_colorama_init

    # colorama_init_once()

    def ask_user_yes_no(msg, timeout=10):
        ensure_printed(f"{msg} (y/n, {timeout}초 내 응답): ", print_color='yellow')
        result = {'answer': None}

        def _get_input():
            try:
                result['answer'] = input().strip().lower()
            except Exception:
                result['answer'] = None

        def _countdown():
            for seconds in reversed(range(1, timeout + 1)):
                ensure_printed(str_working=f"[{PkMessages2025.TIME_LEFT}] [hours:minute:seconds] [{seconds}{PkMessages2025.SECONDS}]")
                time.sleep(1)

        input_thread = threading.Thread(target=_get_input)
        timer_thread = threading.Thread(target=_countdown)
        input_thread.daemon = True
        timer_thread.daemon = True
        input_thread.start()
        timer_thread.start()

        input_thread.join(timeout)

        if result['answer'] is None:
            ensure_printed("시간 초과: 응답이 없어 작업을 건너뜁니다.", print_color='red')
            return 0

        return result['answer'] == 'y'

    try:
        if not does_pnx_exist(pnx=d_working):
            ensure_pnx_made(pnx=d_working, mode='d')

        d_git = rf"{d_working}/.git"

        if not does_pnx_exist(pnx=d_git):
            std_list = ensure_command_excuted_to_os(f'git clone -b {branch_n} {git_repo_url} {d_working}')
            pk_debug_state_for_py_data_type('%%%CLONE%%%', std_list)

            if any("fatal:" in line.lower() for line in std_list):
                ensure_printed(f"Git clone 실패: {std_list}", print_color='red')
                return
        else:
            pk_chdir(d_dst=d_working)
            std_list = ensure_command_excuted_to_os(f'git pull origin {branch_n}')
            pk_debug_state_for_py_data_type('%%%PULL%%%', std_list)

            if any("couldn't find remote ref" in line.lower() for line in std_list):
                ensure_printed(f"브랜치 '{branch_n}' 이(가) 원격 레포지토리에 없습니다.", print_color='red')
                if ask_user_yes_no(f"브랜치 '{branch_n}' 를 새로 만드시겠습니까?"):
                    std_list = ensure_command_excuted_to_os(f'git checkout -b {branch_n}')
                    pk_debug_state_for_py_data_type('%%%CHECKOUT_NEW_BRANCH%%%', std_list)

                    std_list = ensure_command_excuted_to_os(f'git push -u origin {branch_n}')
                    pk_debug_state_for_py_data_type('%%%PUSH_NEW_BRANCH%%%', std_list)

                    if any("error:" in line.lower() or "failed to push" in line.lower() for line in std_list):
                        ensure_printed(f"브랜치 푸시 실패: {std_list}", print_color='red')

                        if ask_user_yes_no("커밋이 없어서 푸시에 실패한 것 같습니다. 빈 커밋을 생성할까요?"):
                            std_list = ensure_command_excuted_to_os('git commit --allow-empty -m "init empty commit"')
                            pk_debug_state_for_py_data_type('%%%EMPTY_COMMIT%%%', std_list)

                            std_list = ensure_command_excuted_to_os(f'git push -u origin {branch_n}')
                            pk_debug_state_for_py_data_type('%%%PUSH_AFTER_EMPTY_COMMIT%%%', std_list)

                            if any("error:" in line.lower() or "failed to push" in line.lower() for line in std_list):
                                ensure_printed(f"빈 커밋 후 푸시도 실패했습니다: {std_list}", print_color='red')
                                return
                        else:
                            ensure_printed("사용자가 빈 커밋 생성을 취소했습니다.", print_color='red')
                            return
                else:
                    ensure_printed("사용자가 브랜치 생성을 취소했습니다.", print_color='red')
                    return
            elif any("fatal:" in line.lower() for line in std_list):
                ensure_printed(f"Git pull 실패: {std_list}", print_color='red')
                return

        ensure_printed(f"Git 작업 완료: {d_working} {'%%%FOO%%%' if LTA else ''}", print_color='green')

    except Exception:
        ensure_printed(f"{traceback.format_exc()} {'%%%FOO%%%' if LTA else ''}", print_color='red')
