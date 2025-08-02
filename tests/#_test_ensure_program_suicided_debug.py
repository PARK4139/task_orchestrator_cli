#!/usr/bin/env python3
"""
ensure_program_suicided 함수 디버깅 테스트
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_printed import ensure_printed

def test_ensure_program_suicided_debug():
    """ensure_program_suicided 함수 디버깅"""
    ensure_printed("🔍 ensure_program_suicided 디버깅", print_color="blue")
    ensure_printed("=" * 50, print_color="blue")
    
    # 현재 파일 경로
    current_file = __file__
    ensure_printed(f"📁 현재 파일: {current_file}", print_color="blue")
    
    # 1. get_pnx_os_style 테스트
    ensure_printed("1. get_pnx_os_style 테스트...", print_color="yellow")
    try:
        from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
        
        os_style_path = get_pnx_os_style(current_file)
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
    
    # 3. get_window_matches 테스트
    ensure_printed("3. get_window_matches 테스트...", print_color="yellow")
    try:
        from pkg_py.functions_split.ensure_process_killed_by_window_title_seg import get_window_matches
        
        matches = get_window_matches(nx_name)
        ensure_printed(f"📊 찾은 창 개수: {len(matches)}", print_color="blue")
        
        for i, (hwnd, title, similarity) in enumerate(matches[:5]):  # 상위 5개만 표시
            ensure_printed(f"  {i+1}. [{hwnd}] {title} (유사도: {similarity})", print_color="blue")
            
    except Exception as e:
        ensure_printed(f"❌ get_window_matches 실패: {e}", print_color="red")
    
    # 4. 개선된 매칭 로직 테스트
    ensure_printed("4. 개선된 매칭 로직 테스트...", print_color="yellow")
    try:
        improved_matches = get_improved_window_matches(nx_name)
        ensure_printed(f"📊 개선된 매칭 개수: {len(improved_matches)}", print_color="blue")
        
        for i, (hwnd, title, similarity) in enumerate(improved_matches[:5]):
            ensure_printed(f"  {i+1}. [{hwnd}] {title} (유사도: {similarity})", print_color="blue")
            
    except Exception as e:
        ensure_printed(f"❌ 개선된 매칭 실패: {e}", print_color="red")
    
    ensure_printed("=" * 50, print_color="blue")
    ensure_printed("🔍 디버깅 완료", print_color="blue")

def get_improved_window_matches(window_title_seg: str):
    """개선된 창 매칭 함수 - 더 정확한 매칭"""
    import win32gui
    
    matches = []
    
    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                # 더 정확한 매칭 로직
                similarity = calculate_similarity(window_title_seg, title)
                if similarity > 0.5:  # 유사도 임계값
                    matches.append((hwnd, title, similarity))
    
    win32gui.EnumWindows(enum_handler, None)
    matches.sort(key=lambda x: x[2], reverse=True)
    return matches

def calculate_similarity(target: str, window_title: str) -> float:
    """창 제목과 타겟의 유사도 계산"""
    target_lower = target.lower()
    title_lower = window_title.lower()
    
    # 1. 정확한 파일명 매칭 (확장자 제외)
    target_name = os.path.splitext(target)[0].lower()
    title_words = title_lower.split()
    
    # 파일명이 창 제목에 정확히 포함되는지 확인
    if target_name in title_words:
        return 1.0
    
    # 2. 부분 문자열 매칭 (하지만 더 엄격하게)
    if target_lower in title_lower:
        # 파일명이 창 제목의 시작이나 끝에 있는지 확인
        if title_lower.startswith(target_lower) or title_lower.endswith(target_lower):
            return 0.9
        # 중간에 있는 경우는 낮은 점수
        return 0.6
    
    # 3. 단어 단위 매칭
    target_words = target_name.split('_')  # 언더스코어로 분리
    matched_words = sum(1 for word in target_words if word in title_words)
    if matched_words > 0:
        return 0.3 + (matched_words / len(target_words)) * 0.4
    
    return 0.0

if __name__ == "__main__":
    test_ensure_program_suicided_debug() 