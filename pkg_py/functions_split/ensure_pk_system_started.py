from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
from pkg_py.functions_split.ensure_fzf_windows_compatible import run_fzf_windows_interactive
from pkg_py.functions_split.get_fzf_options_customized_optimized import get_fzf_options_customized_optimized


@ensure_seconds_measured
def ensure_pk_system_started(loop_mode=None, pk_file_list=None):
    import inspect
    import os
    import subprocess
    import time

    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
    from pkg_py.functions_split.fallback_choice import fallback_choice
    from pkg_py.functions_split.get_f_historical import ensure_history_file_pnx_got
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_fzf_command import get_fzf_command
    from pkg_py.functions_split.get_last_history import get_last_history
    from pkg_py.functions_split.get_project_info_from_pyproject import get_project_info_from_pyproject
    from pkg_py.functions_split.get_sorted_pk_file_list import get_excutable_pk_system_processes
    from pkg_py.functions_split.get_value_completed_v4 import get_value_completed_v4
    from pkg_py.functions_split.save_to_history import save_to_history
    from pkg_py.system_object.etc import pk_
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025
    func_n = inspect.currentframe().f_code.co_name

    #  디버그: 함수 호출 확인
    ensure_printed(f" ensure_pk_system_started 함수 호출됨 (최적화 버전)", print_color='green')

    def get_smart_file_selection(pk_file_list, last_selected, prefix):
        try:
            # 파일 이름만 추출 (prefix 제거)
            display_names = [os.path.basename(p).removeprefix(prefix) for p in pk_file_list]

            # 마지막 선택 파일이 있으면 기본값으로 설정
            default_query = ""
            if last_selected and last_selected in pk_file_list:
                default_query = os.path.basename(last_selected).removeprefix(prefix)
                ensure_printed(f" 마지막 선택: {default_query}", print_color='cyan')

            ensure_printed(f" Tab으로 자동완성하여 파일을 선택하세요!", print_color='cyan')
            ensure_printed(f" 총 {len(display_names)}개 파일 중에서 선택", print_color='green')
            ensure_printed(f" 사용법: 파일명 타이핑 → Tab으로 자동완성 → Enter로 실행", print_color='yellow')

            # get_value_completed_v4 사용 - Tab 자동완성 지원
            selected_name = get_value_completed_v4(
                message=f" 파일 선택",
                option_values=display_names
            )

            if not selected_name:
                ensure_printed(f" 선택이 취소되었습니다.", print_color='red')
                return None

            # 선택된 이름으로 전체 경로 찾기
            selected_file = next(
                (p for p in pk_file_list if os.path.basename(p) == f"{prefix}{selected_name}"),
                None
            )

            if selected_file:
                ensure_printed(f" 선택됨: {selected_name}", print_color='green')
                return selected_file
            else:
                ensure_printed(f" 파일을 찾을 수 없습니다: {prefix}{selected_name}", print_color='red')
                return None

        except Exception as e:
            ensure_printed(f" 파일 선택 중 오류: {e}", print_color='red')
            ensure_printed(f" 기본 fallback 모드로 전환합니다.", print_color='yellow')
            return fallback_choice(pk_file_list, last_selected)

    while True:
        step_start = time.time()

        #  파일 목록 준비
        prefix = pk_
        if pk_file_list is None:
            pk_file_list = get_excutable_pk_system_processes()

        if LTA:
            try:
                #  LTA 모드에서 refactor 파일 추가
                # refactor_files = get_refactor_py_file_list()
                # pk_file_list += refactor_files
                # ensure_printed(f" refactor 파일 {len(refactor_files)}개 추가됨", print_color='cyan')
                pass
            except Exception as e:
                ensure_printed(f"️ refactor 파일 추가 실패: {e}", print_color='yellow')

        if not pk_file_list:
            ensure_printed(f" 실행 가능한 {prefix}*.py 파일이 없습니다.", print_color='red')
            return False

        ensure_printed(f" {len(pk_file_list)}개의 파일을 발견했습니다.", print_color='green')

        # ️ 설정 옵션들
        last_selected_guide_mode = True if LTA else False
        window_front_mode = False

        #  히스토리 처리
        last_selected = None
        history_file = None
        if last_selected_guide_mode:
            key_name = "last_selected"
            history_file = ensure_history_file_pnx_got(file_id=get_file_id(key_name, func_n))
            last_selected = get_last_history(history_file)

        #  fzf 실행
        file_to_execute = None
        fzf_cmd = get_fzf_command()

        # fzf_cmd 검증 및 처리 (v7 안전장치)
        fzf_executable = None
        if fzf_cmd:
            if isinstance(fzf_cmd, list):
                # 리스트가 반환된 경우 - 잘못된 캐시 결과
                ensure_printed(f"️ fzf_cmd가 잘못된 리스트로 반환됨: {fzf_cmd[:2] if len(fzf_cmd) > 2 else fzf_cmd}", print_color='yellow')
                fzf_executable = None
            elif isinstance(fzf_cmd, str):
                # fzf 실행파일인지 확인 (pk 파일이 아닌지)
                if fzf_cmd.endswith('.py') or 'pk_ensure' in fzf_cmd or 'pkg_py' in fzf_cmd:
                    ensure_printed(f"️ 잘못된 fzf 경로 감지됨: {fzf_cmd}", print_color='yellow')
                    fzf_executable = None
                elif (fzf_cmd.lower().endswith('fzf.exe') or
                      fzf_cmd.lower().endswith('fzf') or
                      'fzf' in fzf_cmd.lower()):
                    fzf_executable = fzf_cmd
                    ensure_printed(f" 유효한 fzf 발견: {fzf_executable}", print_color='green')
                else:
                    ensure_printed(f"️ 의심스러운 fzf 경로: {fzf_cmd}", print_color='yellow')
                    fzf_executable = None
            else:
                ensure_printed(f"️ 예상치 못한 fzf_cmd 타입: {type(fzf_cmd)}", print_color='yellow')
                fzf_executable = None

        # ️ fzf 실행 시간 측정 시작점 정의
        fzf_start = time.time()

        if fzf_executable and os.path.exists(fzf_executable):
            try:
                ensure_printed(f" fzf를 사용하여 파일을 선택합니다...", print_color='yellow')

                # ️ 렌더링 시간 측정 시작
                render_start = time.time()

                #  1단계: 데이터 준비 시간 측정
                data_prep_start = time.time()
                display_names = [os.path.basename(p).removeprefix(prefix) for p in pk_file_list]
                fzf_input = "\n".join(display_names)
                data_prep_time = time.time() - data_prep_start
                ensure_printed(f" [렌더링 1단계] 데이터 준비: {data_prep_time:.4f}초 ({len(display_names)}개 파일)", print_color='blue')

                # 디버깅: 처음 몇 개 파일명 확인
                ensure_printed(f" 처음 3개 파일: {display_names[:3]}", print_color='cyan')

                #  2단계: 명령어 준비 시간 측정
                cmd_prep_start = time.time()
                project_info = get_project_info_from_pyproject()
                if project_info:
                    project_name = project_info.get("name", "pk_system")
                    project_version = project_info.get("version", "unknown")
                    prompt_text = f"{project_name} v{project_version}> "
                else:
                    prompt_text = f"{PkMessages2025.COMMANDS}> "

                cmd = [fzf_executable] + get_fzf_options_customized_optimized(prompt_text)

                # 마지막 선택 파일 쿼리 설정 (자동 선택하되 Enter 필요)
                if last_selected_guide_mode and last_selected and last_selected in pk_file_list:
                    fname = os.path.basename(last_selected).removeprefix(prefix)
                    cmd += ["--query", fname]
                    ensure_printed(f" 마지막 선택: {fname} (Enter로 실행)", print_color='cyan')

                cmd_prep_time = time.time() - cmd_prep_start
                ensure_printed(f" [렌더링 2단계] 명령어 준비: {cmd_prep_time:.4f}초", print_color='blue')

                #  3단계: Windows 호환 fzf 실행
                process_start = time.time()
                ensure_printed(f" Windows 호환 fzf UI 렌더링 시작 - {len(display_names)}개 파일", print_color='cyan')
                ensure_printed(f" 파일을 선택하고 Enter를 눌러주세요", print_color='yellow')

                # Windows 호환 fzf 실행
                returncode, out, err = run_fzf_windows_interactive(fzf_input, cmd[1:])  # cmd[0]은 'fzf'이므로 제외

                process_start_time = time.time() - process_start
                ensure_printed(f" [렌더링 3단계] Windows 호환 fzf 실행: {process_start_time:.4f}초", print_color='blue')

                #  전체 렌더링 시간 요약
                total_render_time = time.time() - render_start
                ensure_printed(f" [렌더링 전체] 총 렌더링 시간: {total_render_time:.4f}초", print_color='green')

                # 결과 처리 로직 (사용자 Enter 확인)
                if returncode == 0 and out.strip():
                    selected_name = out.strip()
                    ensure_printed(f" fzf에서 선택됨: '{selected_name}' (Enter 확인됨)", print_color='cyan')

                    file_to_execute = next(
                        (p for p in pk_file_list if os.path.basename(p) == f"{prefix}{selected_name}"),
                        None
                    )
                    if file_to_execute:
                        ensure_printed(f" 파일 매칭 성공: {selected_name}", print_color='green')
                    else:
                        ensure_printed(f" 파일 매칭 실패: {selected_name}", print_color='red')
                        ensure_printed(f" 가능한 파일들: {display_names[:5]}...", print_color='yellow')
                elif returncode == 130:  # Ctrl+C
                    ensure_printed(f"ℹ️ 사용자가 Ctrl+C로 취소했습니다.", print_color='yellow')
                    file_to_execute = None
                elif returncode != 0:
                    ensure_printed(f" fzf 오류 (code {returncode}): {err}", print_color='red')
                    file_to_execute = None
                else:
                    ensure_printed(f"ℹ️ 사용자가 선택을 취소했습니다.", print_color='yellow')
                    file_to_execute = None

            except Exception as e:
                ensure_printed(f" fzf 실행 실패: {e}", print_color='red')
                ensure_printed(f" 자동완성 모드로 전환합니다.", print_color='yellow')
                file_to_execute = get_smart_file_selection(pk_file_list, last_selected, prefix)
        else:
            ensure_printed(f"ℹ️ fzf를 찾을 수 없습니다. 자동완성 모드를 사용합니다.", print_color='yellow')
            file_to_execute = get_smart_file_selection(pk_file_list, last_selected, prefix)

        # ️ fzf 실행 시간 측정 (전체)
        fzf_time = time.time() - fzf_start
        ensure_printed(f"️ 전체 선택 시간: {fzf_time:.3f}초", print_color='cyan')

        #  실행 취소 처리
        if not file_to_execute:
            ensure_printed(f" 실행이 취소되었습니다.", print_color='red')
            return False

        #  파일 존재 확인
        if not os.path.exists(file_to_execute):
            ensure_printed(f" 파일이 존재하지 않습니다: {file_to_execute}", print_color='red')
            return False

        #  히스토리 저장
        if last_selected_guide_mode and history_file:
            try:
                save_to_history(contents_to_save=file_to_execute, history_file=history_file)
                ensure_printed(f" 히스토리 저장됨", print_color='cyan')
            except Exception as e:
                ensure_printed(f"️ 히스토리 저장 실패: {e}", print_color='yellow')

        #  파일 실행 (성능 최적화)
        file_to_execute = os.path.normpath(file_to_execute)
        file_title = os.path.basename(file_to_execute)

        if file_title.startswith(prefix):
            file_title = file_title.removeprefix(prefix)

        ensure_printed(f" 실행 중: {file_title}", print_color='green')

        # 성능 최적화: uv run 대신 직접 python 사용
        # 운영체제별 최적화된 실행
        if os.name == 'nt':  # Windows
            cmd = f'start "" cmd.exe /k "python "{file_to_execute}""'
            ensure_printed(f" Windows 최적화 실행", print_color='blue')
        elif os.name == 'posix':  # Linux/WSL
            cmd = f'python3 "{file_to_execute}"'
            ensure_printed(f" Linux/WSL 최적화 실행", print_color='blue')
        else:
            cmd = f'python "{file_to_execute}"'
            ensure_printed(f" 기본 실행", print_color='yellow')

        # 비동기 실행으로 UI 블로킹 방지
        subprocess.Popen(cmd, shell=True)
        ensure_printed(f" 비동기 실행 완료", print_color='green')

        #  실행 후 대기
        ensure_slept(milliseconds=500)

        #  윈도우 포커스 (옵션)
        if window_front_mode:
            ensure_window_to_front(window_title_seg=rf"{file_to_execute}")

        #  전체 실행 시간 측정
        total_time = time.time() - step_start
        ensure_printed(f" 총 실행 시간: {total_time:.3f}초", print_color='green')

        #  루프 모드 처리
        if not loop_mode:
            ensure_printed(f" v7 실행 완료", print_color='green')
            return True
        else:
            ensure_printed(f" loop_mode - 다음 실행 대기 중...", print_color='yellow')
            pk_file_list = None  # 다음 루프에서 새로 가져오기
