#!/bin/bash

# API 테스트 스크립트

echo "🧪 API 테스트를 시작합니다..."
echo ""

# API Gateway 기본 테스트
echo "1️⃣ API Gateway 기본 테스트"
curl -s http://localhost:8000/ | jq . || echo "API Gateway에 연결할 수 없습니다."

echo ""
echo "2️⃣ 투자 타이밍 추천 테스트"
curl -s "http://localhost:8000/api/v1/recommend/invest-timing?asset_name=삼성전자&current_price=75000&investment_amount=1000000&risk_tolerance=medium" | jq . || echo "투자 타이밍 추천 API에 연결할 수 없습니다."

echo ""
echo "3️⃣ 자산 가격 조회 테스트"
curl -s "http://localhost:8000/api/v1/price/asset?asset_name=삼성전자&asset_type=stock" | jq . || echo "자산 가격 조회 API에 연결할 수 없습니다."

echo ""
echo "4️⃣ 뉴스 크롤링 테스트"
curl -s "http://localhost:8000/api/v1/news/crawl?keywords=삼성전자,투자&max_articles=5" | jq . || echo "뉴스 크롤링 API에 연결할 수 없습니다."

echo ""
echo "5️⃣ 회수 타이밍 추천 테스트"
curl -s "http://localhost:8000/api/v1/recommend/harvest-timing?asset_name=삼성전자&current_price=80000&purchase_price=70000&purchase_date=2024-01-01T00:00:00&current_profit_rate=14.3&target_profit_rate=20.0" | jq . || echo "회수 타이밍 추천 API에 연결할 수 없습니다."

echo ""
echo "✅ API 테스트가 완료되었습니다!"
echo ""
echo "📚 API 문서: http://localhost:8000/docs"
echo "🛠️  더 많은 테스트: curl -X GET 'http://localhost:8000/docs'" 