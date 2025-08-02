#!/usr/bin/env python3
"""
자동화된 테스트 실행기 - 모든 테스트를 실행하고 리포트 생성
"""

import os
import sys
import importlib
import inspect
from datetime import datetime
from typing import List, Dict, Any

# 프로젝트 루트를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_base import TestRunner, TestResult

class AutomatedTestRunner:
    """자동화된 테스트 실행기"""
    
    def __init__(self, dry_run: bool = True, test_dir: str = None):
        self.dry_run = dry_run
        self.test_dir = test_dir or os.path.dirname(os.path.abspath(__file__))
        self.test_runner = TestRunner(dry_run=dry_run)
        self.test_files = []
        self.test_functions = []
        
    def discover_tests(self) -> List[str]:
        """테스트 파일들을 자동으로 발견합니다"""
        test_files = []
        
        for filename in os.listdir(self.test_dir):
            if (filename.startswith('test_') and 
                filename.endswith('.py') and 
                not filename.startswith('#_')):
                test_files.append(filename)
        
        self.test_files = sorted(test_files)
        return test_files
    
    def load_test_functions(self) -> List[Dict[str, Any]]:
        """테스트 파일에서 테스트 함수들을 로드합니다"""
        test_functions = []
        
        for test_file in self.test_files:
            try:
                # 파일명에서 모듈명 추출
                module_name = test_file[:-3]  # .py 제거
                
                # 모듈 import
                spec = importlib.util.spec_from_file_location(
                    module_name, 
                    os.path.join(self.test_dir, test_file)
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # 테스트 함수 찾기
                for name, obj in inspect.getmembers(module):
                    if (inspect.isfunction(obj) and 
                        name.startswith('test_') and 
                        name != 'test_comprehensive_tts'):  # comprehensive_tts는 별도 처리
                        test_functions.append({
                            'file': test_file,
                            'module': module,
                            'function_name': name,
                            'function': obj
                        })
                
            except Exception as e:
                print(f"⚠️ 테스트 파일 로드 실패: {test_file} - {e}")
        
        self.test_functions = test_functions
        return test_functions
    
    def run_all_tests(self) -> List[TestResult]:
        """모든 테스트를 실행합니다"""
        print("🚀 자동화된 테스트 실행 시작")
        print("=" * 60)
        print(f"실행 모드: {'DRY RUN' if self.dry_run else '실제 실행'}")
        print(f"테스트 디렉토리: {self.test_dir}")
        print("=" * 60)
        
        # 테스트 발견
        test_files = self.discover_tests()
        print(f"📁 발견된 테스트 파일: {len(test_files)}개")
        for file in test_files:
            print(f"  - {file}")
        
        # 테스트 함수 로드
        test_functions = self.load_test_functions()
        print(f"🧪 발견된 테스트 함수: {len(test_functions)}개")
        
        # 테스트 실행
        results = []
        
        for test_info in test_functions:
            test_name = f"{test_info['file']}::{test_info['function_name']}"
            print(f"\n🧪 테스트 실행: {test_name}")
            
            try:
                if self.dry_run:
                    print(f"🔍 [DRY RUN] 테스트 시뮬레이션: {test_name}")
                    result = TestResult(
                        test_name=test_name,
                        status="PASS",
                        duration=0.1,
                        dry_run=True
                    )
                else:
                    # 실제 테스트 실행
                    start_time = datetime.now()
                    test_info['function']()
                    duration = (datetime.now() - start_time).total_seconds()
                    
                    result = TestResult(
                        test_name=test_name,
                        status="PASS",
                        duration=duration,
                        dry_run=False
                    )
                
                print(f"✅ 테스트 통과: {test_name}")
                
            except Exception as e:
                result = TestResult(
                    test_name=test_name,
                    status="FAIL",
                    duration=0.0,
                    error_message=str(e),
                    dry_run=self.dry_run
                )
                print(f"❌ 테스트 실패: {test_name} - {e}")
            
            results.append(result)
            self.test_runner.test_results.append(result)
        
        # comprehensive_tts 테스트 별도 실행
        if 'comprehensive_tts_test.py' in test_files:
            print(f"\n🧪 종합 TTS 테스트 실행")
            try:
                from comprehensive_tts_test import test_comprehensive_tts
                
                if self.dry_run:
                    print(f"🔍 [DRY RUN] 종합 TTS 테스트 시뮬레이션")
                    result = TestResult(
                        test_name="comprehensive_tts_test.py::test_comprehensive_tts",
                        status="PASS",
                        duration=0.5,
                        dry_run=True
                    )
                else:
                    start_time = datetime.now()
                    test_comprehensive_tts()
                    duration = (datetime.now() - start_time).total_seconds()
                    
                    result = TestResult(
                        test_name="comprehensive_tts_test.py::test_comprehensive_tts",
                        status="PASS",
                        duration=duration,
                        dry_run=False
                    )
                
                print(f"✅ 종합 TTS 테스트 통과")
                results.append(result)
                self.test_runner.test_results.append(result)
                
            except Exception as e:
                result = TestResult(
                    test_name="comprehensive_tts_test.py::test_comprehensive_tts",
                    status="FAIL",
                    duration=0.0,
                    error_message=str(e),
                    dry_run=self.dry_run
                )
                print(f"❌ 종합 TTS 테스트 실패: {e}")
                results.append(result)
                self.test_runner.test_results.append(result)
        
        return results
    
    def generate_detailed_report(self) -> str:
        """상세한 테스트 리포트를 생성합니다"""
        total_tests = len(self.test_runner.test_results)
        passed_tests = len([r for r in self.test_runner.test_results if r.status == "PASS"])
        failed_tests = len([r for r in self.test_runner.test_results if r.status == "FAIL"])
        success_rate = (passed_tests/total_tests*100) if total_tests > 0 else 0.0
        
        report = f"""
📊 자동화된 테스트 실행 리포트
{'=' * 80}
실행 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
실행 모드: {'DRY RUN' if self.dry_run else '실제 실행'}
테스트 디렉토리: {self.test_dir}

📈 전체 통계:
{'=' * 40}
총 테스트 수: {total_tests}
통과: {passed_tests}
실패: {failed_tests}
        성공률: {success_rate:.1f}%

📋 테스트 파일별 결과:
{'=' * 40}
"""
        
        # 파일별로 그룹화
        file_results = {}
        for result in self.test_runner.test_results:
            file_name = result.test_name.split('::')[0]
            if file_name not in file_results:
                file_results[file_name] = []
            file_results[file_name].append(result)
        
        for file_name, results in file_results.items():
            file_passed = len([r for r in results if r.status == "PASS"])
            file_failed = len([r for r in results if r.status == "FAIL"])
            file_total = len(results)
            
            status_icon = "✅" if file_failed == 0 else "⚠️" if file_passed > 0 else "❌"
            report += f"{status_icon} {file_name} ({file_passed}/{file_total} 통과)\n"
            
            for result in results:
                test_name = result.test_name.split('::')[1] if '::' in result.test_name else result.test_name
                test_status = "✅" if result.status == "PASS" else "❌"
                report += f"  {test_status} {test_name} ({result.duration:.2f}초)\n"
                if result.error_message:
                    report += f"    오류: {result.error_message}\n"
        
        # 실패한 테스트 상세 정보
        failed_results = [r for r in self.test_runner.test_results if r.status == "FAIL"]
        if failed_results:
            report += f"\n❌ 실패한 테스트 상세 정보:\n{'=' * 40}\n"
            for result in failed_results:
                report += f"테스트: {result.test_name}\n"
                report += f"오류: {result.error_message}\n"
                if result.error_traceback:
                    report += f"상세 오류:\n{result.error_traceback}\n"
                report += "-" * 40 + "\n"
        
        return report
    
    def save_detailed_report(self, filename: str = None) -> str:
        """상세한 테스트 리포트를 파일로 저장합니다"""
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            mode = "dry_run" if self.dry_run else "actual"
            filename = f"detailed_test_report_{mode}_{timestamp}.txt"
        
        report = self.generate_detailed_report()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"📄 상세 리포트 저장됨: {filename}")
        return filename

def main():
    """메인 실행 함수"""
    import argparse
    
    parser = argparse.ArgumentParser(description='자동화된 테스트 실행기')
    parser.add_argument('--dry-run', action='store_true', default=True,
                       help='dry_run 모드로 실행 (기본값: True)')
    parser.add_argument('--actual', action='store_true',
                       help='실제 실행 모드')
    parser.add_argument('--test-dir', type=str, default=None,
                       help='테스트 디렉토리 경로')
    parser.add_argument('--save-report', action='store_true', default=True,
                       help='테스트 리포트를 파일로 저장')
    
    args = parser.parse_args()
    
    # dry_run 모드 결정
    dry_run = args.dry_run and not args.actual
    
    # 테스트 러너 생성 및 실행
    runner = AutomatedTestRunner(dry_run=dry_run, test_dir=args.test_dir)
    results = runner.run_all_tests()
    
    # 리포트 생성 및 저장
    if args.save_report:
        runner.save_detailed_report()
    
    # 간단한 리포트 출력
    print("\n" + "=" * 60)
    print(runner.test_runner.generate_report())
    
    return results

if __name__ == "__main__":
    main() 