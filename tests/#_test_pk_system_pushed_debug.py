#!/usr/bin/env python3
"""
pk_ensure_pk_system_pushed.py 파일의 ensure_program_suicided 디버깅 테스트
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed

def test_pk_system_pushed_debug():
    """pk_ensure_pk_system_pushed.py 파일의 ensure_program_suicided 디버깅"""
    ensure_printed("🔍 pk_ensure_pk_system_pushed.py 디버깅", print_color="blue")
    ensure_printed("=" * 60, print_color="blue")
    
    # pk_ensure_pk_system_pushed.py 파일 경로
    target_file = "pkg_py/pk_ensure_pk_system_pushed.py"
    ensure_printed(f"📁 대상 파일: {target_file}", print_color="blue")
    
    # 1. get_pnx_os_style 테스트
    ensure_printed("1. get_pnx_os_style 테스트...", print_color="yellow")
    try:
        from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
        
        os_style_path = get_pnx_os_style(target_file)
        ensure_printed(f"📊 OS 스타일 경로: {os_style_path}", print_color="blue")
        
    except Exception as e:
        ensure_printed(f"❌ get_pnx_os_style 실패: {e}", print_color="red")
    
    # 2. get_nx 테스트
    ensure_printed("2. get_nx 테스트...", print_color="yellow")
    try:
        from pkg_py.functions_split.get_nx import get_nx
        
        nx_name = get_nx(os_style_path)
        ensure_printed(f"📊 NX 이름: {nx_name}", print_color="blue")
        
    except Exception as e:
        ensure_printed(f"❌ get_nx 실패: {e}", print_color="red")
    
    # 3. get_window_matches 테스트 (현재 로직)
    ensure_printed("3. 현재 get_window_matches 테스트...", print_color="yellow")
    try:
        from pkg_py.functions_split.ensure_process_killed_by_window_title_seg import get_window_matches
        
        matches = get_window_matches(nx_name)
        ensure_printed(f"📊 찾은 창 개수: {len(matches)}", print_color="blue")
        
        for i, (hwnd, title, similarity) in enumerate(matches[:10]):  # 상위 10개 표시
            ensure_printed(f"  {i+1}. [{hwnd}] {title} (유사도: {similarity})", print_color="blue")
            
    except Exception as e:
        ensure_printed(f"❌ get_window_matches 실패: {e}", print_color="red")
    
    # 4. 기존 로직으로 테스트 (이전 방식)
    ensure_printed("4. 기존 로직 테스트 (이전 방식)...", print_color="yellow")
    try:
        old_matches = get_old_window_matches(nx_name)
        ensure_printed(f"📊 기존 로직으로 찾은 창 개수: {len(old_matches)}", print_color="blue")
        
        for i, (hwnd, title, similarity) in enumerate(old_matches[:10]):
            ensure_printed(f"  {i+1}. [{hwnd}] {title} (유사도: {similarity})", print_color="blue")
            
    except Exception as e:
        ensure_printed(f"❌ 기존 로직 실패: {e}", print_color="red")
    
    # 5. 더 엄격한 매칭 테스트
    ensure_printed("5. 더 엄격한 매칭 테스트...", print_color="yellow")
    try:
        strict_matches = get_strict_window_matches(nx_name)
        ensure_printed(f"📊 엄격한 매칭으로 찾은 창 개수: {len(strict_matches)}", print_color="blue")
        
        for i, (hwnd, title, similarity) in enumerate(strict_matches[:10]):
            ensure_printed(f"  {i+1}. [{hwnd}] {title} (유사도: {similarity})", print_color="blue")
            
    except Exception as e:
        ensure_printed(f"❌ 엄격한 매칭 실패: {e}", print_color="red")
    
    ensure_printed("=" * 60, print_color="blue")
    ensure_printed("🔍 디버깅 완료", print_color="blue")

def get_old_window_matches(window_title_seg: str):
    """기존 로직 - 단순 부분 문자열 매칭"""
    import win32gui
    
    matches = []
    
    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                is_similar = window_title_seg.lower() in title.lower()
                similarity = is_similar
                matches.append((hwnd, title, similarity))
    
    win32gui.EnumWindows(enum_handler, None)
    matches.sort(key=lambda x: x[2], reverse=True)
    return matches

def get_strict_window_matches(window_title_seg: str):
    """더 엄격한 매칭 - 파일명과 정확히 일치하는 경우만"""
    import win32gui
    import os
    
    matches = []
    
    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                # 파일명 (확장자 제외)
                target_name = os.path.splitext(window_title_seg)[0].lower()
                title_lower = title.lower()
                
                # 정확한 파일명이 창 제목에 포함되는지 확인
                if target_name in title_lower.split():
                    similarity = 1.0
                elif target_name == title_lower:
                    similarity = 1.0
                elif title_lower.startswith(target_name) or title_lower.endswith(target_name):
                    similarity = 0.9
                else:
                    similarity = 0.0
                
                if similarity > 0.8:  # 매우 높은 임계값
                    matches.append((hwnd, title, similarity))
    
    win32gui.EnumWindows(enum_handler, None)
    matches.sort(key=lambda x: x[2], reverse=True)
    return matches

if __name__ == "__main__":
    test_pk_system_pushed_debug() 