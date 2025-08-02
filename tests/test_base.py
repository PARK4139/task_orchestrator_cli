#!/usr/bin/env python3
"""
테스트 기본 클래스 - dry_run 기능 제공
"""

import os
import sys
import time
import traceback
from datetime import datetime
from typing import Any, Dict, List, Optional, Callable
from dataclasses import dataclass, field

# 프로젝트 루트를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@dataclass
class TestResult:
    """테스트 결과를 저장하는 데이터 클래스"""
    test_name: str
    status: str  # 'PASS', 'FAIL', 'SKIP', 'ERROR'
    duration: float
    error_message: Optional[str] = None
    error_traceback: Optional[str] = None
    dry_run: bool = False
    timestamp: datetime = field(default_factory=datetime.now)

class DryRunMixin:
    """dry_run 기능을 제공하는 믹스인 클래스"""
    
    def __init__(self, dry_run: bool = True):
        self.dry_run = dry_run
        self.test_results: List[TestResult] = []
    
    def dry_run_execute(self, func: Callable, *args, **kwargs) -> Any:
        """dry_run 모드에서 함수를 실행하거나 시뮬레이션합니다"""
        if self.dry_run:
            print(f"🔍 [DRY RUN] 실행할 함수: {func.__name__}")
            print(f"🔍 [DRY RUN] 인자: args={args}, kwargs={kwargs}")
            return None
        else:
            return func(*args, **kwargs)
    
    def dry_run_print(self, message: str, print_color: str = "blue"):
        """dry_run 모드에서 출력을 시뮬레이션합니다"""
        if self.dry_run:
            print(f"🔍 [DRY RUN] 출력: {message}")
        else:
            # 실제 출력 로직 (ensure_printed 함수 사용)
            try:
                from pkg_py.functions_split.ensure_printed import ensure_printed
                ensure_printed(message, print_color=print_color)
            except ImportError:
                print(message)
    
    def dry_run_sleep(self, seconds: float):
        """dry_run 모드에서 sleep을 시뮬레이션합니다"""
        if self.dry_run:
            print(f"🔍 [DRY RUN] Sleep: {seconds}초")
        else:
            time.sleep(seconds)

class TestRunner(DryRunMixin):
    """테스트 실행을 관리하는 클래스"""
    
    def __init__(self, dry_run: bool = True):
        super().__init__(dry_run)
        self.start_time = time.time()
    
    def run_test(self, test_func: Callable, test_name: str = None) -> TestResult:
        """개별 테스트를 실행합니다"""
        if test_name is None:
            test_name = test_func.__name__
        
        print(f"\n🧪 테스트 실행: {test_name}")
        print("=" * 60)
        
        start_time = time.time()
        result = TestResult(
            test_name=test_name,
            status="PASS",
            duration=0.0,
            dry_run=self.dry_run
        )
        
        try:
            if self.dry_run:
                print(f"🔍 [DRY RUN] 테스트 함수: {test_func.__name__}")
                # dry_run 모드에서는 함수를 실제로 실행하지 않고 시뮬레이션
                print(f"🔍 [DRY RUN] 테스트 시뮬레이션 완료")
            else:
                test_func()
            
            result.status = "PASS"
            print(f"✅ 테스트 통과: {test_name}")
            
        except Exception as e:
            result.status = "FAIL"
            result.error_message = str(e)
            result.error_traceback = traceback.format_exc()
            print(f"❌ 테스트 실패: {test_name}")
            print(f"❌ 오류: {e}")
            if not self.dry_run:
                print(f"❌ 상세 오류:\n{result.error_traceback}")
        
        result.duration = time.time() - start_time
        self.test_results.append(result)
        
        print(f"⏱️  실행 시간: {result.duration:.2f}초")
        print("=" * 60)
        
        return result
    
    def generate_report(self) -> str:
        """테스트 결과 리포트를 생성합니다"""
        total_time = time.time() - self.start_time
        total_tests = len(self.test_results)
        passed_tests = len([r for r in self.test_results if r.status == "PASS"])
        failed_tests = len([r for r in self.test_results if r.status == "FAIL"])
        success_rate = (passed_tests/total_tests*100) if total_tests > 0 else 0.0
        
        report = f"""
📊 테스트 실행 리포트
{'=' * 60}
실행 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
실행 모드: {'DRY RUN' if self.dry_run else '실제 실행'}
총 테스트 수: {total_tests}
통과: {passed_tests}
실패: {failed_tests}
        성공률: {success_rate:.1f}%
총 실행 시간: {total_time:.2f}초

📋 상세 결과:
{'-' * 60}
"""
        
        for result in self.test_results:
            status_icon = "✅" if result.status == "PASS" else "❌"
            report += f"{status_icon} {result.test_name} ({result.duration:.2f}초)\n"
            if result.error_message:
                report += f"   오류: {result.error_message}\n"
        
        return report
    
    def save_report(self, filename: str = None):
        """테스트 리포트를 파일로 저장합니다"""
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            mode = "dry_run" if self.dry_run else "actual"
            filename = f"test_report_{mode}_{timestamp}.txt"
        
        report = self.generate_report()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"📄 리포트 저장됨: {filename}")
        return filename

# 전역 테스트 러너 인스턴스
test_runner = TestRunner(dry_run=True)

def run_test_with_dry_run(test_func: Callable, test_name: str = None):
    """테스트를 dry_run 모드로 실행하는 편의 함수"""
    return test_runner.run_test(test_func, test_name)

def generate_test_report():
    """전역 테스트 리포트를 생성합니다"""
    return test_runner.generate_report()

def save_test_report(filename: str = None):
    """전역 테스트 리포트를 저장합니다"""
    return test_runner.save_report(filename) 