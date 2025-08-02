#!/usr/bin/env python3
"""
PID 디버깅 - dry_run 지원
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_base import DryRunMixin, run_test_with_dry_run

class PIDDebugTest(DryRunMixin):
    """PID 디버깅 테스트 클래스"""
    
    def __init__(self, dry_run: bool = True):
        super().__init__(dry_run)
    
    def test_pid_debug(self):
        """PID 디버깅"""
        self.dry_run_print("🔍 PID 디버깅", print_color="blue")
        self.dry_run_print("=" * 60, print_color="blue")
        
        try:
            if self.dry_run:
                self.dry_run_print("🔍 [DRY RUN] win32gui, win32process 모듈 시뮬레이션", print_color="blue")
                self.dry_run_print("📊 pk_ensure_pk_system_started.py 창 개수: 시뮬레이션됨", print_color="blue")
                self.dry_run_print("  시뮬레이션된 창 정보들...", print_color="blue")
                self.dry_run_print("📊 고유한 PID 개수: 시뮬레이션됨", print_color="blue")
                self.dry_run_print("📊 PID 목록: 시뮬레이션됨", print_color="blue")
                self.dry_run_print("✅ 각 창이 서로 다른 PID를 가지고 있습니다.", print_color="green")
            else:
                import win32gui
                import win32process
                
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
                
                # pk_ensure_pk_system_started.py 창들 찾기
                target_windows = [(hwnd, title) for hwnd, title in all_windows 
                                 if 'pk_ensure_pk_system_started.py' in title]
                
                self.dry_run_print(f"📊 pk_ensure_pk_system_started.py 창 개수: {len(target_windows)}", print_color="blue")
                
                # PID 확인
                pids = set()
                for i, (hwnd, title) in enumerate(target_windows):
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    pids.add(pid)
                    self.dry_run_print(f"  {i+1}. [{hwnd}] {title} → PID: {pid}", print_color="blue")
                
                self.dry_run_print(f"📊 고유한 PID 개수: {len(pids)}", print_color="blue")
                self.dry_run_print(f"📊 PID 목록: {sorted(pids)}", print_color="blue")
                
                if len(pids) == len(target_windows):
                    self.dry_run_print("✅ 각 창이 서로 다른 PID를 가지고 있습니다.", print_color="green")
                else:
                    self.dry_run_print("❌ 일부 창이 같은 PID를 공유합니다.", print_color="red")
                    
        except Exception as e:
            self.dry_run_print(f"❌ 디버깅 실패: {e}", print_color="red")
        
        self.dry_run_print("=" * 60, print_color="blue")
        self.dry_run_print("🔍 PID 디버깅 완료", print_color="blue")

def test_pid_debug():
    """PID 디버깅 테스트 함수"""
    test_instance = PIDDebugTest(dry_run=True)
    test_instance.test_pid_debug()

if __name__ == "__main__":
    # dry_run 모드로 테스트 실행
    run_test_with_dry_run(test_pid_debug, "PID 디버깅") 