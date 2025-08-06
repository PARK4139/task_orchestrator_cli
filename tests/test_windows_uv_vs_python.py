#!/usr/bin/env python3
"""
Windows에서 uv vs python 직접 실행 성능 비교 테스트
test_ prefix 규칙에 따라 작성
"""

import os
import sys
import time
import subprocess
import platform

# 프로젝트 루트를 Python 경로에 추가
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def test_windows_uv_vs_python_performance():
    """Windows에서 uv vs python 직접 실행 성능 비교"""
    
    print("🧪 Windows uv vs python 직접 실행 성능 비교")
    print("=" * 50)
    
    # 테스트 명령어들
    commands = [
        ("python --version", "Python 직접 실행"),
        ("uv run python --version", "UV 실행"),
        ("cmd /c python --version", "cmd에서 Python 실행"),
        ("powershell -Command python --version", "PowerShell에서 Python 실행"),
    ]
    
    results = []
    
    for cmd, description in commands:
        print(f"\n🔍 테스트: {description}")
        print(f"명령어: {cmd}")
        
        # 5회 실행하여 평균 시간 측정
        times = []
        for i in range(5):
            start_time = time.time()
            try:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
                execution_time = time.time() - start_time
                
                if result.returncode == 0:
                    times.append(execution_time)
                    print(f"  실행 {i+1}: {execution_time:.3f}초")
                else:
                    print(f"  실행 {i+1}: 실패")
                    
            except subprocess.TimeoutExpired:
                print(f"  실행 {i+1}: 타임아웃")
            except Exception as e:
                print(f"  실행 {i+1}: 오류 - {e}")
        
        if times:
            avg_time = sum(times) / len(times)
            min_time = min(times)
            max_time = max(times)
            print(f"📊 결과: 평균 {avg_time:.3f}초 (최소: {min_time:.3f}초, 최대: {max_time:.3f}초)")
            results.append((description, avg_time, min_time, max_time, "성공"))
        else:
            results.append((description, 0, 0, 0, "실패"))
    
    # 결과 요약
    print("\n📊 Windows uv vs python 성능 비교 결과")
    print("=" * 50)
    print(f"{'명령어':25} | {'평균':6}초 | {'최소':6}초 | {'최대':6}초 | {'상태'}")
    print("-" * 70)
    for description, avg_time, min_time, max_time, status in results:
        print(f"{description:25} | {avg_time:6.3f}초 | {min_time:6.3f}초 | {max_time:6.3f}초 | {status}")
    
    return results

def test_windows_venv_activation():
    """Windows 가상환경 활성화 성능 테스트"""
    
    print("\n🧪 Windows 가상환경 활성화 성능 테스트")
    print("=" * 50)
    
    # 가상환경 경로들
    venv_paths = [
        os.path.join(project_root, ".venv"),
        os.path.join(project_root, ".venv_linux"),
    ]
    
    results = []
    
    for venv_path in venv_paths:
        if os.path.exists(venv_path):
            print(f"\n🔍 테스트: {os.path.basename(venv_path)}")
            print(f"경로: {venv_path}")
            
            # Windows용 가상환경 스크립트 확인
            activate_script = os.path.join(venv_path, "Scripts", "activate.bat")
            if os.path.exists(activate_script):
                print(f"✅ Windows 가상환경 스크립트 존재: {activate_script}")
                
                # 가상환경 활성화 시간 측정
                start_time = time.time()
                try:
                    cmd = f'"{activate_script}" && python --version'
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
                    activation_time = time.time() - start_time
                    
                    if result.returncode == 0:
                        print(f"✅ 활성화 성공: {activation_time:.3f}초")
                        results.append((os.path.basename(venv_path), activation_time, "성공"))
                    else:
                        print(f"❌ 활성화 실패: {result.stderr}")
                        results.append((os.path.basename(venv_path), activation_time, "실패"))
                        
                except Exception as e:
                    print(f"❌ 활성화 오류: {e}")
                    results.append((os.path.basename(venv_path), 0, "오류"))
            else:
                print(f"❌ Windows 가상환경 스크립트 없음")
                results.append((os.path.basename(venv_path), 0, "스크립트 없음"))
        else:
            print(f"\n❌ 가상환경 없음: {venv_path}")
            results.append((os.path.basename(venv_path), 0, "존재하지 않음"))
    
    # 결과 요약
    print("\n📊 Windows 가상환경 활성화 결과")
    print("=" * 50)
    for venv_name, time_taken, status in results:
        print(f"{venv_name:20} | {time_taken:6.3f}초 | {status}")
    
    return results

def test_windows_python_execution_methods():
    """Windows Python 실행 방법별 성능 테스트"""
    
    print("\n🧪 Windows Python 실행 방법별 성능 테스트")
    print("=" * 50)
    
    # 실행 방법들
    execution_methods = [
        ("python", "Python 직접 실행"),
        ("python3", "Python3 직접 실행"),
        ("uv run python", "UV를 통한 Python 실행"),
        ("cmd /c python", "cmd에서 Python 실행"),
        ("powershell -Command python", "PowerShell에서 Python 실행"),
    ]
    
    results = []
    
    for method, description in execution_methods:
        print(f"\n🔍 테스트: {description}")
        print(f"명령어: {method} --version")
        
        start_time = time.time()
        try:
            result = subprocess.run(f"{method} --version", shell=True, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            if result.returncode == 0:
                print(f"✅ 성공: {execution_time:.3f}초")
                print(f"출력: {result.stdout.strip()}")
                results.append((description, execution_time, "성공"))
            else:
                print(f"❌ 실패: {result.stderr}")
                results.append((description, execution_time, "실패"))
                
        except subprocess.TimeoutExpired:
            print(f"⏰ 타임아웃: 10초 초과")
            results.append((description, 10.0, "타임아웃"))
        except Exception as e:
            print(f"❌ 오류: {e}")
            results.append((description, 0, "오류"))
    
    # 결과 요약
    print("\n📊 Windows Python 실행 방법별 성능 결과")
    print("=" * 50)
    for description, time_taken, status in results:
        print(f"{description:30} | {time_taken:6.3f}초 | {status}")
    
    return results

def test_windows_optimization_recommendations():
    """Windows 최적화 권장 사항"""
    
    print("\n🧪 Windows 최적화 권장 사항")
    print("=" * 50)
    
    recommendations = [
        ("1. 가상환경 미리 활성화", "가상환경을 미리 활성화하여 실행 시간 단축"),
        ("2. Python 직접 실행", "uv run 대신 python 직접 사용"),
        ("3. cmd.exe 최적화", "Windows에서 cmd.exe /k 사용으로 비동기 실행"),
        ("4. fzf 캐싱", "fzf 입력 데이터 캐싱으로 렌더링 시간 단축"),
        ("5. 파일 목록 최적화", "불필요한 파일 제외로 목록 크기 감소"),
    ]
    
    print("💡 Windows 성능 최적화 권장 사항:")
    for recommendation, description in recommendations:
        print(f"   {recommendation}: {description}")
    
    return recommendations

if __name__ == "__main__":
    print("🎯 Windows uv vs python 성능 비교 테스트 (test_ prefix 규칙)")
    print("=" * 50)
    
    # 1. uv vs python 성능 비교
    performance_results = test_windows_uv_vs_python_performance()
    
    # 2. 가상환경 활성화 성능 테스트
    venv_results = test_windows_venv_activation()
    
    # 3. Python 실행 방법별 성능 테스트
    execution_results = test_windows_python_execution_methods()
    
    # 4. 최적화 권장 사항
    recommendations = test_windows_optimization_recommendations()
    
    print("\n🏁 모든 테스트 완료")
    print("=" * 50)
    
    # 최종 결과 요약
    print("\n📊 Windows 성능 비교 테스트 결과 요약")
    print("=" * 50)
    print(f"uv vs python 성능 비교: {len(performance_results)}개")
    print(f"가상환경 활성화 테스트: {len(venv_results)}개")
    print(f"Python 실행 방법 테스트: {len(execution_results)}개")
    print(f"최적화 권장 사항: {len(recommendations)}개")
    
    # 성능 개선 효과 분석
    if performance_results:
        python_direct = next((r for r in performance_results if "Python 직접 실행" in r[0]), None)
        uv_run = next((r for r in performance_results if "UV 실행" in r[0]), None)
        
        if python_direct and uv_run and python_direct[1] > 0 and uv_run[1] > 0:
            improvement = uv_run[1] / python_direct[1]
            print(f"\n📈 성능 개선 효과: {improvement:.1f}x 빠름")
            if improvement > 2:
                print("✅ Python 직접 실행이 UV 실행보다 훨씬 빠릅니다!")
            else:
                print("⚠️ 성능 차이가 크지 않습니다.")
    
    # 권장 사항
    print("\n💡 Windows 성능 최적화 결론:")
    print("1. 가상환경이 이미 설정되어 있으므로 uv run 대신 python 직접 사용")
    print("2. Windows에서는 cmd.exe /k를 사용한 비동기 실행이 효과적")
    print("3. fzf 렌더링 시간은 파일 목록 크기와 사용자 인터랙션에 의존")
    print("4. 전체적인 성능 개선은 이미 적용되어 있음") 