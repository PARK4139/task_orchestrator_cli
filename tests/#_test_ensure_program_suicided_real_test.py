#!/usr/bin/env python3
"""
실제 ensure_program_suicided 함수 테스트
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed

def test_ensure_program_suicided_real():
    """실제 ensure_program_suicided 함수 테스트"""
    ensure_printed("🔍 실제 ensure_program_suicided 테스트", print_color="blue")
    ensure_printed("=" * 60, print_color="blue")
    
    # 현재 실행 중인 창들을 먼저 확인
    ensure_printed("📋 현재 실행 중인 창들 확인...", print_color="yellow")
    try:
        import win32gui
        
        def enum_windows():
            windows = []
            
            def enum_handler(hwnd, _):
                if win32gui.IsWindowVisible(hwnd):
                    title = win32gui.GetWindowText(hwnd)
                    if title and len(title) > 3:  # 의미있는 제목만
                        windows.append((hwnd, title))
            
            win32gui.EnumWindows(enum_handler, None)
            return windows
        
        current_windows = enum_windows()
        ensure_printed(f"📊 현재 실행 중인 창 개수: {len(current_windows)}", print_color="blue")
        
        # Python 관련 창들만 필터링
        python_windows = [(hwnd, title) for hwnd, title in current_windows 
                         if 'python' in title.lower() or '.py' in title.lower()]
        
        ensure_printed(f"📊 Python 관련 창 개수: {len(python_windows)}", print_color="blue")
        for i, (hwnd, title) in enumerate(python_windows[:10]):
            ensure_printed(f"  {i+1}. [{hwnd}] {title}", print_color="blue")
            
    except Exception as e:
        ensure_printed(f"❌ 창 목록 확인 실패: {e}", print_color="red")
    
    # 실제 ensure_program_suicided 호출 (하지만 실제로는 종료하지 않고 매칭만 확인)
    ensure_printed("🔍 ensure_program_suicided 매칭 확인...", print_color="yellow")
    try:
        from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
        
        # 현재 파일로 테스트
        current_file = __file__
        ensure_printed(f"📁 테스트 파일: {current_file}", print_color="blue")
        
        # ensure_program_suicided 호출 (실제로는 종료하지 않음)
        ensure_program_suicided(current_file)
        
    except Exception as e:
        ensure_printed(f"❌ ensure_program_suicided 실패: {e}", print_color="red")
    
    ensure_printed("=" * 60, print_color="blue")
    ensure_printed("🔍 테스트 완료", print_color="blue")

if __name__ == "__main__":
    test_ensure_program_suicided_real() 