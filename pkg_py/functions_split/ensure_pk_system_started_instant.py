"""
즉시 실행을 위한 최적화된 pk_system 시작 함수
백그라운드 모니터링에서 호출될 때 사용
"""

import os
import subprocess
import time
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_pk_system_started_ultra_fast import ensure_pk_system_started_ultra_fast


def ensure_pk_system_started_instant():
    """
    즉시 실행 버전 - 최소한의 초기화만 수행
    """
    start_time = time.time()
    
    try:
        # 최소한의 로깅만 수행
        ensure_printed(f" 즉시 실행 모드 시작", print_color='green')
        
        # 직접 ultra_fast 함수 호출 (초기화 과정 생략)
        result = ensure_pk_system_started_ultra_fast()
        
        execution_time = time.time() - start_time
        ensure_printed(f" 즉시 실행 완료 (총 시간: {execution_time:.3f}초)", print_color='green')
        
        return result
        
    except Exception as e:
        ensure_printed(f" 즉시 실행 오류: {e}", print_color='red')
        return False


def ensure_pk_system_started_minimal():
    """
    최소한의 초기화로 실행 (가장 빠름)
    """
    start_time = time.time()
    
    try:
        # 기본적인 파일 목록만 가져와서 실행
        from pkg_py.functions_split.get_sorted_pk_file_list import get_excutable_pk_system_processes
        from pkg_py.functions_split.get_value_completed_v4 import get_value_completed_v4
        from pkg_py.system_object.etc import pk_
        
        # 파일 목록 가져오기
        pk_file_list = get_excutable_pk_system_processes()
        
        if not pk_file_list:
            ensure_printed(f" 실행 가능한 파일이 없습니다.", print_color='red')
            return False
            
        # 간단한 선택 UI
        display_names = [os.path.basename(p).removeprefix(pk_) for p in pk_file_list]
        
        selected_name = get_value_completed_v4(
            message=f" 파일 선택 (총 {len(display_names)}개)",
            option_values=display_names
        )
        
        if not selected_name:
            ensure_printed(f" 선택이 취소되었습니다.", print_color='yellow')
            return False
            
        # 파일 실행
        selected_file = next(
            (p for p in pk_file_list if os.path.basename(p) == f"{pk_}{selected_name}"),
            None
        )
        
        if selected_file and os.path.exists(selected_file):
            # 백그라운드에서 실행
            cmd = f'start "" cmd.exe /k "python "{selected_file}""'
            subprocess.Popen(cmd, shell=True)
            
            execution_time = time.time() - start_time
            ensure_printed(f" 최소 실행 완료 (시간: {execution_time:.3f}초)", print_color='green')
            return True
        else:
            ensure_printed(f" 파일을 찾을 수 없습니다.", print_color='red')
            return False
            
    except Exception as e:
        ensure_printed(f" 최소 실행 오류: {e}", print_color='red')
        return False


if __name__ == "__main__":
    # 명령행 인수에 따라 실행 모드 선택
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "minimal":
        ensure_pk_system_started_minimal()
    else:
        ensure_pk_system_started_instant() 