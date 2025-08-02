#!/usr/bin/env python3
"""
간단한 매칭 디버깅 - dry_run 지원
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_base import DryRunMixin, run_test_with_dry_run

class SimpleDebugTest(DryRunMixin):
    """간단한 매칭 디버깅 테스트 클래스"""
    
    def __init__(self, dry_run: bool = True):
        super().__init__(dry_run)
    
    def test_simple_debug(self):
        """간단한 매칭 디버깅"""
        self.dry_run_print("🔍 간단한 매칭 디버깅", print_color="blue")
        self.dry_run_print("=" * 60, print_color="blue")
        
        # 테스트할 파일명
        target_file = "pk_ensure_pk_system_started.py"
        
        # 테스트할 창 제목들
        test_titles = [
            "pk_ensure_pk_system_started.py",  # 정확히 일치
            "pk_ensure_pk_system_started.py - pk_system - Cursor",  # 확장 포함
            "some_other_file.py",  # 다른 파일
            "pk_ensure_pk_system_started",  # 확장자 없음
            "ensure_pk_system_started.py",  # 비슷하지만 다름
        ]
        
        try:
            from pkg_py.functions_split.ensure_process_killed_by_window_title_seg import calculate_similarity
            
            for title in test_titles:
                if self.dry_run:
                    self.dry_run_print(f"파일명: '{target_file}' vs 창제목: '{title}' → 유사도: 계산됨", print_color="blue")
                else:
                    similarity = calculate_similarity(target_file, title)
                    self.dry_run_print(f"파일명: '{target_file}' vs 창제목: '{title}' → 유사도: {similarity}", print_color="blue")
        except ImportError as e:
            self.dry_run_print(f"⚠️ 모듈 import 오류: {e}", print_color="yellow")
        
        self.dry_run_print("=" * 60, print_color="blue")
        self.dry_run_print("🔍 디버깅 완료", print_color="blue")

def test_simple_debug():
    """간단한 매칭 디버깅 테스트 함수"""
    test_instance = SimpleDebugTest(dry_run=True)
    test_instance.test_simple_debug()

if __name__ == "__main__":
    # dry_run 모드로 테스트 실행
    run_test_with_dry_run(test_simple_debug, "간단한 매칭 디버깅") 