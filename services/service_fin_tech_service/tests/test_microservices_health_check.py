"""
마이크로서비스 헬스체크 통합 테스트
"""
import requests
import time
import inspect
from typing import Dict, Any, List


def test_service_health_check(service_name: str, port: int) -> Dict[str, Any]:
    """
    특정 서비스의 헬스체크를 테스트합니다.
    """
    # 현재 함수명을 동적으로 가져오기
    func_n = inspect.currentframe().f_code.co_name
    
    print(f"🔍 {func_n} 함수 실행 - {service_name} (포트: {port})")
    
    try:
        response = requests.get(f"http://localhost:{port}/health", timeout=10)
        
        if response.status_code == 200:
            print(f"✅ {service_name} 헬스체크 성공")
            return {"success": True, "status_code": response.status_code}
        else:
            print(f"❌ {service_name} 헬스체크 실패: {response.status_code}")
            return {"success": False, "status_code": response.status_code}
            
    except requests.exceptions.RequestException as e:
        print(f"❌ {service_name} 연결 실패: {e}")
        return {"success": False, "error": str(e)}


def test_all_microservices() -> List[Dict[str, Any]]:
    """
    모든 마이크로서비스의 헬스체크를 테스트합니다.
    """
    services = [
        {"name": "API Gateway", "port": 8000},
        {"name": "Investment Advisor", "port": 8001},
        {"name": "Market Data", "port": 8002},
        {"name": "News Analyzer", "port": 8003}
    ]
    
    results = []
    
    for service in services:
        result = test_service_health_check(service["name"], service["port"])
        result["service"] = service["name"]
        results.append(result)
        time.sleep(1)  # 요청 간 간격
    
    return results


def main():
    """
    메인 테스트 실행 함수
    """
    # 현재 함수명을 동적으로 가져오기
    func_n = inspect.currentframe().f_code.co_name
    
    print(f"🚀 {func_n} 함수 시작")
    print("=" * 60)
    
    # 서비스 시작 대기
    print("⏳ 서비스 시작 대기 중...")
    time.sleep(10)
    
    # 모든 서비스 테스트
    results = test_all_microservices()
    
    # 결과 요약
    print("\n📊 테스트 결과:")
    success_count = 0
    
    for result in results:
        status = "✅ 성공" if result["success"] else "❌ 실패"
        print(f"{result['service']}: {status}")
        if result["success"]:
            success_count += 1
    
    print(f"\n총 {len(results)}개 서비스 중 {success_count}개 성공")
    
    if success_count == len(results):
        print("\n🎉 모든 마이크로서비스가 정상 작동합니다!")
        return 0
    else:
        print(f"\n💥 {len(results) - success_count}개 서비스에 문제가 있습니다.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) 