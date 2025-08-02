#!/usr/bin/env python3
"""
ensure_program_suicided 함수 상세 디버깅
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed

def test_ensure_program_suicided_detailed():
    """ensure_program_suicided 함수 상세 디버깅"""
    ensure_printed("🔍 ensure_program_suicided 상세 디버깅", print_color="blue")
    ensure_printed("=" * 60, print_color="blue")
    
    # 1. 현재 실행 중인 모든 창 확인
    ensure_printed("1. 현재 실행 중인 모든 창 확인...", print_color="yellow")
    try:
        import win32gui
        
        def get_all_windows():
            windows = []
            
            def enum_handler(hwnd, _):
                if win32gui.IsWindowVisible(hwnd):
                    title = win32gui.GetWindowText(hwnd)
                    if title and len(title) > 2:
                        windows.append((hwnd, title))
            
            win32gui.EnumWindows(enum_handler, None)
            return windows
        
        all_windows = get_all_windows()
        ensure_printed(f"📊 전체 창 개수: {len(all_windows)}", print_color="blue")
        
        # Python 관련 창들만 필터링
        python_windows = [(hwnd, title) for hwnd, title in all_windows 
                         if 'python' in title.lower() or '.py' in title.lower() or 'pk_' in title.lower()]
        
        ensure_printed(f"📊 Python/PK 관련 창 개수: {len(python_windows)}", print_color="blue")
        for i, (hwnd, title) in enumerate(python_windows):
            ensure_printed(f"  {i+1}. [{hwnd}] {title}", print_color="blue")
            
    except Exception as e:
        ensure_printed(f"❌ 창 목록 확인 실패: {e}", print_color="red")
    
    # 2. 특정 파일명으로 매칭 테스트
    ensure_printed("2. 특정 파일명 매칭 테스트...", print_color="yellow")
    test_files = [
        "pk_ensure_pk_system_pushed.py",
        "pk_ensure_pk_system_started.py", 
        "ensure_file_found.py",
        "test_ensure_program_suicided_detailed_debug.py"
    ]
    
    for test_file in test_files:
        ensure_printed(f"📁 테스트 파일: {test_file}", print_color="blue")
        try:
            from pkg_py.functions_split.ensure_process_killed_by_window_title_seg import get_window_matches
            
            matches = get_window_matches(test_file)
            ensure_printed(f"  📊 매칭된 창 개수: {len(matches)}", print_color="blue")
            
            for i, (hwnd, title, similarity) in enumerate(matches):
                ensure_printed(f"    {i+1}. [{hwnd}] {title} (유사도: {similarity})", print_color="blue")
                
        except Exception as e:
            ensure_printed(f"  ❌ 매칭 실패: {e}", print_color="red")
    
    # 3. 실제 ensure_program_suicided 호출 시뮬레이션
    ensure_printed("3. ensure_program_suicided 시뮬레이션...", print_color="yellow")
    try:
        from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
        
        # 현재 파일로 테스트
        current_file = __file__
        ensure_printed(f"📁 시뮬레이션 파일: {current_file}", print_color="blue")
        
        # 실제 호출 (하지만 실제로는 종료하지 않음)
        ensure_printed("⚠️ 실제 ensure_program_suicided 호출 중...", print_color="red")
        ensure_program_suicided(current_file)
        
    except Exception as e:
        ensure_printed(f"❌ 시뮬레이션 실패: {e}", print_color="red")
    
    ensure_printed("=" * 60, print_color="blue")
    ensure_printed("🔍 상세 디버깅 완료", print_color="blue")

if __name__ == "__main__":
    test_ensure_program_suicided_detailed() 