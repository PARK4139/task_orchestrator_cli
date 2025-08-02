#!/usr/bin/env python3
"""
창 제목 디버깅 - dry_run 지원
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_base import DryRunMixin, run_test_with_dry_run

class WindowTitleDebugTest(DryRunMixin):
    """창 제목 디버깅 테스트 클래스"""
    
    def __init__(self, dry_run: bool = True):
        super().__init__(dry_run)
    
    def test_window_title_debug(self):
        """창 제목 디버깅"""
        self.dry_run_print("🔍 창 제목 디버깅", print_color="blue")
        self.dry_run_print("=" * 60, print_color="blue")
        
        try:
            if self.dry_run:
                self.dry_run_print("🔍 [DRY RUN] win32gui 모듈 시뮬레이션", print_color="blue")
                self.dry_run_print("📊 Python 관련 창 개수: 시뮬레이션됨", print_color="blue")
                
                # 시뮬레이션된 창들
                simulated_windows = [
                    (12345, "pk_ensure_pk_system_started.py - pk_system - Cursor"),
                    (12346, "python.exe - pk_ensure_pk_system_started.py"),
                    (12347, "test_window_title_debug.py - Visual Studio Code"),
                    (12348, "Python Console - pk_system"),
                    (12349, "main.py - PyCharm")
                ]
                
                for i, (hwnd, title) in enumerate(simulated_windows):
                    self.dry_run_print(f"  {i+1}. [{hwnd}] '{title}'", print_color="blue")
                    
                    # 파일명 추출 (테스트용)
                    filename = "pk_ensure_pk_system_started.py"  # 테스트용 파일명
                    filename_no_ext = os.path.splitext(filename)[0]
                    
                    self.dry_run_print(f"     파일명: '{filename}'", print_color="blue")
                    self.dry_run_print(f"     파일명(확장자 제외): '{filename_no_ext}'", print_color="blue")
                    self.dry_run_print(f"     유사도: 시뮬레이션됨", print_color="blue")
                    
                    # 단어 분리 테스트
                    title_words = title.lower().split()
                    self.dry_run_print(f"     창 제목 단어들: {title_words}", print_color="blue")
                    
                    # 정확한 매칭 테스트
                    if filename_no_ext.lower() in title_words:
                        self.dry_run_print(f"     ✅ 파일명이 창 제목 단어에 포함됨", print_color="green")
                    else:
                        self.dry_run_print(f"     ❌ 파일명이 창 제목 단어에 포함되지 않음", print_color="red")
                    
                    # 시작/끝 매칭 테스트
                    if title.lower().startswith(f"{filename_no_ext.lower()} "):
                        self.dry_run_print(f"     ✅ 창 제목이 파일명으로 시작함", print_color="green")
                    elif title.lower().endswith(f" {filename_no_ext.lower()}"):
                        self.dry_run_print(f"     ✅ 창 제목이 파일명으로 끝남", print_color="green")
                    else:
                        self.dry_run_print(f"     ❌ 창 제목이 파일명으로 시작/끝하지 않음", print_color="red")
                    
                    self.dry_run_print("", print_color="blue")
            else:
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
                
                # 모든 Python 관련 창들 확인
                python_windows = [(hwnd, title) for hwnd, title in all_windows 
                                 if 'python' in title.lower() or '.py' in title.lower()]
                
                self.dry_run_print(f"📊 Python 관련 창 개수: {len(python_windows)}", print_color="blue")
                target_windows = python_windows[:5]  # 처음 5개만 테스트
                for i, (hwnd, title) in enumerate(target_windows):
                    self.dry_run_print(f"  {i+1}. [{hwnd}] '{title}'", print_color="blue")
                    
                    # 파일명 추출 (테스트용)
                    filename = "pk_ensure_pk_system_started.py"  # 테스트용 파일명
                    filename_no_ext = os.path.splitext(filename)[0]
                    
                    self.dry_run_print(f"     파일명: '{filename}'", print_color="blue")
                    self.dry_run_print(f"     파일명(확장자 제외): '{filename_no_ext}'", print_color="blue")
                    
                    # 매칭 테스트
                    from pkg_py.functions_split.ensure_process_killed_by_window_title_seg import calculate_similarity
                    
                    similarity = calculate_similarity(filename, title)
                    self.dry_run_print(f"     유사도: {similarity}", print_color="blue")
                    
                    # 단어 분리 테스트
                    title_words = title.lower().split()
                    self.dry_run_print(f"     창 제목 단어들: {title_words}", print_color="blue")
                    
                    # 정확한 매칭 테스트
                    if filename_no_ext.lower() in title_words:
                        self.dry_run_print(f"     ✅ 파일명이 창 제목 단어에 포함됨", print_color="green")
                    else:
                        self.dry_run_print(f"     ❌ 파일명이 창 제목 단어에 포함되지 않음", print_color="red")
                    
                    # 시작/끝 매칭 테스트
                    if title.lower().startswith(f"{filename_no_ext.lower()} "):
                        self.dry_run_print(f"     ✅ 창 제목이 파일명으로 시작함", print_color="green")
                    elif title.lower().endswith(f" {filename_no_ext.lower()}"):
                        self.dry_run_print(f"     ✅ 창 제목이 파일명으로 끝남", print_color="green")
                    else:
                        self.dry_run_print(f"     ❌ 창 제목이 파일명으로 시작/끝하지 않음", print_color="red")
                    
                    self.dry_run_print("", print_color="blue")
            
        except Exception as e:
            self.dry_run_print(f"❌ 디버깅 실패: {e}", print_color="red")
        
        self.dry_run_print("=" * 60, print_color="blue")
        self.dry_run_print("🔍 창 제목 디버깅 완료", print_color="blue")

def test_window_title_debug():
    """창 제목 디버깅 테스트 함수"""
    test_instance = WindowTitleDebugTest(dry_run=True)
    test_instance.test_window_title_debug()

if __name__ == "__main__":
    # dry_run 모드로 테스트 실행
    run_test_with_dry_run(test_window_title_debug, "창 제목 디버깅") 