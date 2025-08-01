"""
API 엔드포인트 통합 테스트
"""
import requests
import time
import inspect
from typing import Dict, Any, List


def test_investment_advisor_endpoints() -> List[Dict[str, Any]]:
    """
    Investment Advisor API 엔드포인트를 테스트합니다.
    """
    # 현재 함수명을 동적으로 가져오기
    func_n = inspect.currentframe().f_code.co_name
    
    print(f"🔍 {func_n} 함수 실행 시작")
    
    endpoints = [
        {
            "name": "투자 타이밍 분석",
            "url": "http://localhost:8000/api/v1/recommend/invest-timing",
            "params": {"asset_name": "삼성전자"}
        },
        {
            "name": "수확 타이밍 계산",
            "url": "http://localhost:8000/api/v1/recommend/harvest-timing",
            "params": {"asset_name": "삼성전자", "investment_amount": 1000000}
        }
    ]
    
    results = []
    
    for endpoint in endpoints:
        try:
            response = requests.get(endpoint["url"], params=endpoint["params"], timeout=10)
            
            if response.status_code == 200:
                print(f"✅ {endpoint['name']} 성공")
                results.append({
                    "success": True,
                    "endpoint": endpoint["name"],
                    "status_code": response.status_code
                })
            else:
                print(f"❌ {endpoint['name']} 실패: {response.status_code}")
                results.append({
                    "success": False,
                    "endpoint": endpoint["name"],
                    "status_code": response.status_code
                })
                
        except requests.exceptions.RequestException as e:
            print(f"❌ {endpoint['name']} 연결 실패: {e}")
            results.append({
                "success": False,
                "endpoint": endpoint["name"],
                "error": str(e)
            })
    
    return results


def test_market_data_endpoints() -> List[Dict[str, Any]]:
    """
    Market Data API 엔드포인트를 테스트합니다.
    """
    # 현재 함수명을 동적으로 가져오기
    func_n = inspect.currentframe().f_code.co_name
    
    print(f"🔍 {func_n} 함수 실행 시작")
    
    endpoints = [
        {
            "name": "자산 가격 조회",
            "url": "http://localhost:8000/api/v1/finance/price",
            "params": {"symbol": "005930.KS"}
        },
        {
            "name": "시장 데이터 조회",
            "url": "http://localhost:8000/api/v1/finance/market-data",
            "params": {"market": "KOSPI"}
        }
    ]
    
    results = []
    
    for endpoint in endpoints:
        try:
            response = requests.get(endpoint["url"], params=endpoint["params"], timeout=10)
            
            if response.status_code == 200:
                print(f"✅ {endpoint['name']} 성공")
                results.append({
                    "success": True,
                    "endpoint": endpoint["name"],
                    "status_code": response.status_code
                })
            else:
                print(f"❌ {endpoint['name']} 실패: {response.status_code}")
                results.append({
                    "success": False,
                    "endpoint": endpoint["name"],
                    "status_code": response.status_code
                })
                
        except requests.exceptions.RequestException as e:
            print(f"❌ {endpoint['name']} 연결 실패: {e}")
            results.append({
                "success": False,
                "endpoint": endpoint["name"],
                "error": str(e)
            })
    
    return results


def test_news_analyzer_endpoints() -> List[Dict[str, Any]]:
    """
    News Analyzer API 엔드포인트를 테스트합니다.
    """
    # 현재 함수명을 동적으로 가져오기
    func_n = inspect.currentframe().f_code.co_name
    
    print(f"🔍 {func_n} 함수 실행 시작")
    
    endpoints = [
        {
            "name": "뉴스 크롤링",
            "url": "http://localhost:8000/api/v1/news/crawl",
            "params": {"keyword": "삼성전자", "limit": 5}
        },
        {
            "name": "뉴스 분석",
            "url": "http://localhost:8000/api/v1/news/analysis",
            "params": {"keyword": "삼성전자"}
        }
    ]
    
    results = []
    
    for endpoint in endpoints:
        try:
            response = requests.get(endpoint["url"], params=endpoint["params"], timeout=10)
            
            if response.status_code == 200:
                print(f"✅ {endpoint['name']} 성공")
                results.append({
                    "success": True,
                    "endpoint": endpoint["name"],
                    "status_code": response.status_code
                })
            else:
                print(f"❌ {endpoint['name']} 실패: {response.status_code}")
                results.append({
                    "success": False,
                    "endpoint": endpoint["name"],
                    "status_code": response.status_code
                })
                
        except requests.exceptions.RequestException as e:
            print(f"❌ {endpoint['name']} 연결 실패: {e}")
            results.append({
                "success": False,
                "endpoint": endpoint["name"],
                "error": str(e)
            })
    
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
    print("⏳ API 서비스 시작 대기 중...")
    time.sleep(10)
    
    # 각 서비스별 테스트 실행
    investment_results = test_investment_advisor_endpoints()
    market_results = test_market_data_endpoints()
    news_results = test_news_analyzer_endpoints()
    
    # 모든 결과 합치기
    all_results = investment_results + market_results + news_results
    
    # 결과 요약
    print("\n📊 테스트 결과:")
    success_count = 0
    
    for result in all_results:
        status = "✅ 성공" if result["success"] else "❌ 실패"
        print(f"{result['endpoint']}: {status}")
        if result["success"]:
            success_count += 1
    
    print(f"\n총 {len(all_results)}개 엔드포인트 중 {success_count}개 성공")
    
    if success_count == len(all_results):
        print("\n🎉 모든 API 엔드포인트가 정상 작동합니다!")
        return 0
    else:
        print(f"\n💥 {len(all_results) - success_count}개 엔드포인트에 문제가 있습니다.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) 