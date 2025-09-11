from functools import lru_cache

from sources.functions.ensure_seconds_measured import ensure_seconds_measured

# 전역 캐시
_FILE_LIST_CACHE = {}
_CACHE_TIMESTAMP = 0
_CACHE_DURATION = 30  # 30초 캐시


class UltraFastFzfProcessor:
    """초고속 fzf 처리기"""

    def __init__(self, fzf_executable, file_list, last_selected=None):
        from functions.get_nx import get_nx

        from sources.objects.pk_etc import pk_
        self.fzf_executable = fzf_executable
        self.file_list = file_list
        self.last_selected = last_selected
        self.filenames_to_display = [get_nx(p).removeprefix(pk_) for p in file_list]

    def build_ultra_fast_fzf_command(self):
        from functions.get_nx import get_nx

        from sources.functions.get_fzf_options_customized_optimized import get_fzf_options_customized_optimized
        from sources.objects.pk_etc import pk_
        """초고속 fzf 명령어 구성"""

        cmd = [self.fzf_executable] + get_fzf_options_customized_optimized()

        # 마지막 선택 파일 쿼리 설정
        if self.last_selected and self.last_selected in self.file_list:
            fname = get_nx(self.last_selected).removeprefix(pk_)
            cmd += ["--query", fname]

        return cmd

    def run_ultra_fast_fzf(self):
        import subprocess

        import logging
        """초고속 fzf 실행"""
        fzf_input = '\n'.join(self.filenames_to_display)
        cmd = self.build_ultra_fast_fzf_command()

        proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            #  추가 최적화
            bufsize=1,  # 라인 버퍼링
            universal_newlines=True,  # 텍스트 모드
        )

        logging.debug(f"초고속 UI 렌더링 시작")
        logging.debug(f"파일을 선택하고 Enter를 눌러주세요")

        # 사용자 입력 대기
        out, err = proc.communicate(input=fzf_input)

        return proc.returncode, out.strip(), err


@lru_cache(maxsize=1)  # task_orchestrator_cli_option
def get_cached_files(d_working):
    from functions.get_pnxs import get_pnxs
    import time

    import logging
    """파일 목록 캐싱 (30초)"""
    global _FILE_LIST_CACHE, _CACHE_TIMESTAMP

    current_time = time.time()

    # 캐시가 유효한지 확인
    if current_time - _CACHE_TIMESTAMP < _CACHE_DURATION and _FILE_LIST_CACHE:
        logging.debug(f"캐시된 파일 목록 사용 (총 {len(_FILE_LIST_CACHE)}개)")
        return _FILE_LIST_CACHE

    # 새로운 파일 목록 가져오기
    files = get_pnxs(d_working=d_working)
    _FILE_LIST_CACHE = files
    _CACHE_TIMESTAMP = current_time

    logging.debug(f"새로운 파일 목록 로딩 (총 {len(files)}개)")
    return files


def get_filenames_to_display(files):
    from functions.get_nx import get_nx
    return [get_nx(p) for p in files]


def get_smart_file_selection_fast(pk_files, last_selected):
    import logging
    from functions.get_nx import get_nx
    from sources.functions.ensure_value_advanced_fallback_via_input import ensure_value_advanced_fallback_via_input
    """초고속 파일 선택 로직"""
    try:
        display_names = get_filenames_to_display(files=pk_files)

        if last_selected and last_selected in pk_files:
            default_query = get_nx(last_selected)
            logging.debug(f"마지막 선택: {default_query}")

        logging.debug(f"Tab으로 자동완성하여 파일을 선택하세요!")
        logging.debug(f"총 {len(display_names)}개 파일 중에서 선택")

        selected_name = ensure_value_completed_return_core(
            message=f" 파일 선택",
            options=display_names
        )

        if not selected_name:
            logging.debug(f"선택이 취소되었습니다.")
            return None

        selected_file = next((p for p in pk_files if get_nx(p) == selected_name), None)
        if selected_file:
            logging.debug(f"선택됨: {selected_name}")
            return selected_file
        else:
            logging.debug(f"파일을 찾을 수 없습니다: {selected_name}")
            return None

    except Exception as e:
        logging.debug(f"파일 선택 중 오류: {e}")
        return ensure_value_advanced_fallback_via_input(pk_files, last_selected)


@ensure_seconds_measured
def ensure_task_orchestrator_cli_started(loop_mode=None, pk_files=None, test_mode=False):
    import logging
    import os
    import subprocess
    import time

    from functions.get_caller_n import get_caller_n
    from functions.get_nx import get_nx
    from objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_WRAPPERS
    from sources.functions.ensure_slept import ensure_slept
    from sources.functions.ensure_window_to_front import ensure_window_to_front
    from sources.functions.get_f_historical import ensure_history_file_pnx_return
    from sources.functions.get_file_id import get_file_id
    from sources.functions.get_fzf_command import get_fzf_command
    from sources.functions.get_last_history import get_last_history
    from sources.functions.save_to_history import save_to_history
    from sources.objects.pk_etc import pk_
    from sources.objects.pk_local_test_activate import LTA
    """초고속 pk 시스템 시작 함수 - 극한 렌더링 최적화"""

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    while True:
        step_start = time.time()

        #  파일 목록 준비 (캐싱 적용)
        if pk_files is None:
            pk_files = get_cached_files(D_TASK_ORCHESTRATOR_CLI_WRAPPERS)

        if not pk_files:
            logging.debug(f"실행 가능한 래퍼 파일이 없습니다.")
            return False

        logging.debug(f"{len(pk_files)}개의 파일을 발견했습니다.")

        # ️ pk_options
        # last_selected_guide_mode = True if LTA else True
        last_selected_guide_mode = True if LTA else False
        window_front_mode = False

        #  히스토리 처리 (최적화)
        last_selected = None
        history_file = None
        if last_selected_guide_mode:
            key_name = "last_selected"
            history_file = ensure_history_file_pnx_return(file_id=get_file_id(key_name, func_n))
            last_selected = get_last_history(history_file)

        #  초고속 fzf 실행
        file_to_execute = None
        fzf_cmd = get_fzf_command()

        if fzf_cmd and os.path.exists(fzf_cmd):
            try:
                processor = UltraFastFzfProcessor(fzf_cmd, pk_files, last_selected)
                returncode, selected_name, err = processor.run_ultra_fast_fzf()

                if returncode == 0 and selected_name:
                    logging.debug(f"selected_name='{selected_name}'")

                    for pk_file in pk_files:
                        prefix = "pk_"
                        logging.debug(rf'selected_name.removeprefix(prefix)={selected_name.removeprefix(prefix)}')
                        logging.debug(rf'get_nx(pk_file).removeprefix(prefix)={get_nx(pk_file).removeprefix(prefix)}')
                        logging.debug(rf'get_nx(pk_file).removeprefix(prefix) == selected_name.removeprefix(prefix)={get_nx(pk_file).removeprefix(prefix) == selected_name.removeprefix(prefix)}')
                        if get_nx(pk_file).removeprefix(prefix) == selected_name.removeprefix(prefix):
                            # logging.debug(rf'selected_name.removeprefix(prefix)={selected_name.removeprefix(prefix)}')
                            # logging.debug(rf'get_nx(pk_file).removeprefix(prefix)={get_nx(pk_file).removeprefix(prefix)}')
                            # logging.debug(rf'get_nx(pk_file).removeprefix(prefix) == selected_name.removeprefix(prefix)={get_nx(pk_file).removeprefix(prefix) == selected_name.removeprefix(prefix)}')
                            file_to_execute = pk_file

                    if file_to_execute:
                        logging.debug(f"matched: {selected_name}")
                    else:
                        logging.debug(f"not matched: {selected_name}")
                        file_to_execute = None
                elif returncode == 130:  # Ctrl+C
                    logging.debug(f"ℹ️ 사용자가 Ctrl+C로 취소했습니다.")
                    file_to_execute = None
                elif returncode != 0:
                    logging.debug(f"fzf 오류 (code {returncode}): {err}")
                    file_to_execute = None
                else:
                    logging.debug(f"ℹ️ 사용자가 선택을 취소했습니다.")
                    file_to_execute = None

            except Exception as e:
                logging.debug(f"fzf 실행 실패: {e}")
                logging.debug(f"자동완성 모드로 전환합니다.")
                file_to_execute = get_smart_file_selection_fast(pk_files, last_selected)
        else:
            logging.debug(f"ℹ️ fzf를 찾을 수 없습니다. 자동완성 모드를 사용합니다.")
            file_to_execute = get_smart_file_selection_fast(pk_files, last_selected)

        #  실행 취소 처리
        if not file_to_execute:
            logging.debug(f"실행이 취소되었습니다.")
            return False

        #  파일 존재 확인
        if not os.path.exists(file_to_execute):
            logging.debug(f"파일이 존재하지 않습니다: {file_to_execute}")
            return False

        #  히스토리 저장
        if last_selected_guide_mode and history_file:
            try:
                save_to_history(contents_to_save=file_to_execute, history_file=history_file)
                logging.debug(f"히스토리 저장됨")
            except Exception as e:
                logging.debug(f"️ 히스토리 저장 실패: {e}")

        #  극한 성능 최적화 실행
        file_to_execute = os.path.normpath(file_to_execute)
        filename_to_display = get_nx(file_to_execute)
        if filename_to_display.startswith(pk_):
            filename_to_display = filename_to_display.removeprefix(pk_)
        logging.debug(f"실행 중: {filename_to_display}")
        if os.name == 'nt':  # Windows
            cmd = f'start "" cmd.exe /k "python "{file_to_execute}""'
            logging.debug(f"Windows 극한 최적화 실행")
        elif os.name == 'posix':  # Linux/WSL
            cmd = f'python3 "{file_to_execute}"'
            logging.debug(f"Linux/WSL 극한 최적화 실행")
        else:
            cmd = f'python "{file_to_execute}"'
            logging.debug(f"기본 실행")

        #  비동기 실행으로 UI 블로킹 방지
        subprocess.Popen(cmd, shell=True)
        logging.debug(f"극한 최적화 실행 완료")

        #  실행 후 대기 (최소화)
        ensure_slept(milliseconds=200)  # 500ms → 200ms로 단축

        #  윈도우 포커스
        if window_front_mode:
            ensure_window_to_front(rf"{file_to_execute}")

        #  전체 실행 시간 측정
        total_time = time.time() - step_start
        logging.debug(f"총 실행 시간: {total_time:.3f}초")

        #  루프 모드 처리
        if not loop_mode:
            logging.debug(f"초고속 버전 실행 완료")
            return True
        else:
            logging.debug(f"loop_mode - 다음 실행 대기 중...")
            pk_files = None  # 다음 루프에서 새로 가져오기


def ensure_value_completed_return_core(message, options, test_mode=False):
    from pathlib import Path

    from prompt_toolkit import prompt
    from prompt_toolkit.completion import WordCompleter, FuzzyCompleter

    from functions.get_caller_n import get_caller_n
    from sources.functions.ensure_task_orchestrator_cli_exit_silent import ensure_task_orchestrator_cli_exit_silent
    from sources.functions.ensure_spoken import ensure_spoken
    from sources.functions.is_path_like import is_path_like
    from sources.objects.pk_map_texts import PkTexts

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    if message.strip() == "x":
        ensure_spoken(f"{func_n}() exited(intended)")
        return None

    seen = set()
    deduped = []
    options = options + [PkTexts.SHUTDOWN]
    for option in options:
        # None 값은 건너뛰기
        if option is None:
            continue
        styled = option
        if isinstance(option, str):
            if is_path_like(option):
                styled = Path(option)
        if styled not in seen:
            seen.add(styled)
            deduped.append(styled)

    # fzf 스타일 실시간 검색 완성 기능 유지
    completer = FuzzyCompleter(WordCompleter(deduped, ignore_case=True))

    # 원본 상태로 복원 - 기본 prompt_toolkit 사용
    option_selected = prompt(
        message + " ",
        completer=completer,
    )

    if option_selected.strip() == PkTexts.SHUTDOWN:
        ensure_task_orchestrator_cli_exit_silent()
        return
    return option_selected

# below codes annotated for some duration for deprecated
# if __name__ == '__main__':
#     ensure_task_orchestrator_cli_started()
