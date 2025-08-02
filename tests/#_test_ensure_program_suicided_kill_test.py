#!/usr/bin/env python3
"""
실제 창 닫기 테스트
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed

def test_ensure_program_suicided_kill():
    """실제 창 닫기 테스트"""
    ensure_printed("🔍 실제 창 닫기 테스트", print_color="blue")
    ensure_printed("=" * 60, print_color="blue")
    
    # 1. 현재 실행 중인 창들 확인
    ensure_printed("1. 현재 실행 중인 창들 확인...", print_color="yellow")
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
        
        # pk_ensure_pk_system_pushed.py 창 찾기
        target_windows = [(hwnd, title) for hwnd, title in all_windows 
                         if 'pk_ensure_pk_system_pushed.py' in title]
        
        ensure_printed(f"📊 pk_ensure_pk_system_pushed.py 창 개수: {len(target_windows)}", print_color="blue")
        for i, (hwnd, title) in enumerate(target_windows):
            ensure_printed(f"  {i+1}. [{hwnd}] {title}", print_color="blue")
            
    except Exception as e:
        ensure_printed(f"❌ 창 목록 확인 실패: {e}", print_color="red")
        return
    
    # 2. 실제 ensure_program_suicided 호출
    ensure_printed("2. 실제 ensure_program_suicided 호출...", print_color="yellow")
    try:
        from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
        
        # pk_ensure_pk_system_pushed.py 파일 경로
        target_file = "pkg_py/pk_ensure_pk_system_pushed.py"
        ensure_printed(f"📁 대상 파일: {target_file}", print_color="blue")
        
        # 실제 호출
        ensure_printed("⚠️ 실제 ensure_program_suicided 호출 중...", print_color="red")
        ensure_program_suicided(target_file)
        
    except Exception as e:
        ensure_printed(f"❌ ensure_program_suicided 실패: {e}", print_color="red")
    
    # 3. 호출 후 창 상태 확인
    ensure_printed("3. 호출 후 창 상태 확인...", print_color="yellow")
    try:
        all_windows_after = get_all_windows()
        target_windows_after = [(hwnd, title) for hwnd, title in all_windows_after 
                               if 'pk_ensure_pk_system_pushed.py' in title]
        
        ensure_printed(f"📊 호출 후 pk_ensure_pk_system_pushed.py 창 개수: {len(target_windows_after)}", print_color="blue")
        for i, (hwnd, title) in enumerate(target_windows_after):
            ensure_printed(f"  {i+1}. [{hwnd}] {title}", print_color="blue")
            
        # 창이 닫혔는지 확인
        if len(target_windows) > len(target_windows_after):
            ensure_printed("✅ 창이 성공적으로 닫혔습니다!", print_color="green")
        else:
            ensure_printed("❌ 창이 닫히지 않았습니다.", print_color="red")
            
    except Exception as e:
        ensure_printed(f"❌ 호출 후 확인 실패: {e}", print_color="red")
    
    ensure_printed("=" * 60, print_color="blue")
    ensure_printed("🔍 창 닫기 테스트 완료", print_color="blue")

if __name__ == "__main__":
    test_ensure_program_suicided_kill() 