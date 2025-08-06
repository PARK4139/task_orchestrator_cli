from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
import time
import os
import subprocess
import inspect
import threading
from functools import lru_cache

from pkg_py.functions_split.get_fzf_options_customized_optimized import get_fzf_options_customized_optimized
from pkg_py.functions_split.get_project_info_from_pyproject import get_project_info_from_pyproject
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.etc import pk_
from pkg_py.functions_split.fallback_choice import fallback_choice
from pkg_py.functions_split.get_value_completed_v4 import get_value_completed_v4
from pkg_py.functions_split.get_f_historical import ensure_history_file_pnx_got
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_fzf_command import get_fzf_command
from pkg_py.functions_split.get_last_history import get_last_history
from pkg_py.functions_split.save_to_history import save_to_history
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.ensure_slept import ensure_slept
from pkg_py.functions_split.get_sorted_pk_file_list import get_excutable_pk_system_processes
from pkg_py.functions_split.ensure_printed import ensure_printed

# 전역 캐시
_FILE_LIST_CACHE = {}
_CACHE_TIMESTAMP = 0
_CACHE_DURATION = 30  # 30초 캐시

class UltraFastFzfProcessor:
    """초고속 fzf 처리기"""
    
    def __init__(self, fzf_executable, file_list, last_selected=None):
        self.fzf_executable = fzf_executable
        self.file_list = file_list
        self.last_selected = last_selected
        self.display_names = [os.path.basename(p).removeprefix(pk_) for p in file_list]
        
    def build_ultra_fast_fzf_command(self):
        """초고속 fzf 명령어 구성"""





        cmd = [self.fzf_executable] +  get_fzf_options_customized_optimized()
        
        # 마지막 선택 파일 쿼리 설정
        if self.last_selected and self.last_selected in self.file_list:
            fname = os.path.basename(self.last_selected).removeprefix(pk_)
            cmd += ["--query", fname]
            
        return cmd
    
    def run_ultra_fast_fzf(self):
        """초고속 fzf 실행"""
        fzf_input = '\n'.join(self.display_names)
        cmd = self.build_ultra_fast_fzf_command()
        
        #  프로세스 시작 최적화
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
        
        ensure_printed(f" 초고속 UI 렌더링 시작", print_color='green')
        ensure_printed(f" 파일을 선택하고 Enter를 눌러주세요", print_color='yellow')
        
        # 사용자 입력 대기
        out, err = proc.communicate(input=fzf_input)
        
        return proc.returncode, out.strip(), err

@lru_cache(maxsize=1)
def get_cached_file_list():
    """파일 목록 캐싱 (30초)"""
    global _FILE_LIST_CACHE, _CACHE_TIMESTAMP
    
    current_time = time.time()
    
    # 캐시가 유효한지 확인
    if current_time - _CACHE_TIMESTAMP < _CACHE_DURATION and _FILE_LIST_CACHE:
        ensure_printed(f" 캐시된 파일 목록 사용 (총 {len(_FILE_LIST_CACHE)}개)", print_color='cyan')
        return _FILE_LIST_CACHE
    
    # 새로운 파일 목록 가져오기
    file_list = get_excutable_pk_system_processes()
    _FILE_LIST_CACHE = file_list
    _CACHE_TIMESTAMP = current_time
    
    ensure_printed(f" 새로운 파일 목록 로딩 (총 {len(file_list)}개)", print_color='green')
    return file_list

def get_smart_file_selection_fast(pk_file_list, last_selected, prefix):
    """초고속 파일 선택 로직"""
    try:
        display_names = [os.path.basename(p).removeprefix(prefix) for p in pk_file_list]
        
        if last_selected and last_selected in pk_file_list:
            default_query = os.path.basename(last_selected).removeprefix(prefix)
            ensure_printed(f" 마지막 선택: {default_query}", print_color='cyan')

        ensure_printed(f" Tab으로 자동완성하여 파일을 선택하세요!", print_color='cyan')
        ensure_printed(f" 총 {len(display_names)}개 파일 중에서 선택", print_color='green')

        selected_name = get_value_completed_v4(
            message=f" 파일 선택",
            option_values=display_names
        )

        if not selected_name:
            ensure_printed(f" 선택이 취소되었습니다.", print_color='red')
            return None

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
        return fallback_choice(pk_file_list, last_selected)

@ensure_seconds_measured
def ensure_pk_system_started_ultra_fast(loop_mode=None, pk_file_list=None):
    """초고속 pk 시스템 시작 함수 - 극한 렌더링 최적화"""
    
    func_n = inspect.currentframe().f_code.co_name
    
    #  디버그: 함수 호출 확인
    ensure_printed(f" ensure_pk_system_started_ultra_fast 함수 호출됨 (초고속 버전)", print_color='green')

    while True:
        step_start = time.time()

        #  파일 목록 준비 (캐싱 적용)
        if pk_file_list is None:
            pk_file_list = get_cached_file_list()

        if LTA:
            try:
                pass
            except Exception as e:
                ensure_printed(f"️ refactor 파일 추가 실패: {e}", print_color='yellow')

        if not pk_file_list:
            ensure_printed(f" 실행 가능한 {pk_}*.py 파일이 없습니다.", print_color='red')
            return False

        ensure_printed(f" {len(pk_file_list)}개의 파일을 발견했습니다.", print_color='green')

        # ️ 설정 옵션들
        last_selected_guide_mode = True if LTA else False
        window_front_mode = False

        #  히스토리 처리 (최적화)
        last_selected = None
        history_file = None
        if last_selected_guide_mode:
            key_name = "last_selected"
            history_file = ensure_history_file_pnx_got(file_id=get_file_id(key_name, func_n))
            last_selected = get_last_history(history_file)

        #  초고속 fzf 실행
        file_to_execute = None
        fzf_cmd = get_fzf_command()
        
        if fzf_cmd and os.path.exists(fzf_cmd):
            try:
                processor = UltraFastFzfProcessor(fzf_cmd, pk_file_list, last_selected)
                returncode, selected_name, err = processor.run_ultra_fast_fzf()
                
                if returncode == 0 and selected_name:
                    ensure_printed(f" fzf에서 선택됨: '{selected_name}'", print_color='cyan')
                    file_to_execute = next(
                        (p for p in pk_file_list if os.path.basename(p) == f"{pk_}{selected_name}"),
                        None
                    )
                    if file_to_execute:
                        ensure_printed(f" 파일 매칭 성공: {selected_name}", print_color='green')
                    else:
                        ensure_printed(f" 파일 매칭 실패: {selected_name}", print_color='red')
                        file_to_execute = None
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
                file_to_execute = get_smart_file_selection_fast(pk_file_list, last_selected, pk_)
        else:
            ensure_printed(f"ℹ️ fzf를 찾을 수 없습니다. 자동완성 모드를 사용합니다.", print_color='yellow')
            file_to_execute = get_smart_file_selection_fast(pk_file_list, last_selected, pk_)

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

        #  파일 실행 (극한 최적화)
        file_to_execute = os.path.normpath(file_to_execute)
        file_title = os.path.basename(file_to_execute)

        if file_title.startswith(pk_):
            file_title = file_title.removeprefix(pk_)

        ensure_printed(f" 실행 중: {file_title}", print_color='green')
        
        #  극한 성능 최적화 실행
        if os.name == 'nt':  # Windows
            cmd = f'start "" cmd.exe /k "python "{file_to_execute}""'
            ensure_printed(f" Windows 극한 최적화 실행", print_color='blue')
        elif os.name == 'posix':  # Linux/WSL
            cmd = f'python3 "{file_to_execute}"'
            ensure_printed(f" Linux/WSL 극한 최적화 실행", print_color='blue')
        else:
            cmd = f'python "{file_to_execute}"'
            ensure_printed(f" 기본 실행", print_color='yellow')
        
        #  비동기 실행으로 UI 블로킹 방지
        subprocess.Popen(cmd, shell=True)
        ensure_printed(f" 극한 최적화 실행 완료", print_color='green')

        #  실행 후 대기 (최소화)
        ensure_slept(milliseconds=200)  # 500ms → 200ms로 단축

        #  윈도우 포커스 (옵션)
        if window_front_mode:
            ensure_window_to_front(window_title_seg=rf"{file_to_execute}")

        #  전체 실행 시간 측정
        total_time = time.time() - step_start
        ensure_printed(f" 총 실행 시간: {total_time:.3f}초", print_color='green')

        #  루프 모드 처리
        if not loop_mode:
            ensure_printed(f" 초고속 버전 실행 완료", print_color='green')
            return True
        else:
            ensure_printed(f" loop_mode - 다음 실행 대기 중...", print_color='yellow')
            pk_file_list = None  # 다음 루프에서 새로 가져오기

# 편의 함수
def ensure_pk_system_started_ultra():
    """초고속 버전 실행"""
    return ensure_pk_system_started_ultra_fast() 