#!/usr/bin/env python3
"""
Smart Person AI 서비스 테스트 스크립트

모든 서비스의 기본 기능을 테스트하는 스크립트
"""

import httpx
import asyncio
import json
from pathlib import Path

# 테스트 설정
BASE_URL = "http://localhost:8000"
SERVICES = {
    "gateway": "http://localhost:8000",
    "ai_image": "http://localhost:8001", 
    "ai_book": "http://localhost:8002",
    "excel_automation": "http://localhost:8011",
    "web_crawler": "http://localhost:8012",
    "payment": "http://localhost:8021"
}

async def test_service_health():
    """모든 서비스 헬스체크"""
    print("🔍 Testing service health...")
    
    async with httpx.AsyncClient() as client:
        for service_name, service_url in SERVICES.items():
            try:
                response = await client.get(f"{service_url}/health", timeout=5.0)
                if response.status_code == 200:
                    print(f"   ✅ {service_name}: Healthy")
                else:
                    print(f"   ❌ {service_name}: Unhealthy (Status: {response.status_code})")
            except Exception as e:
                print(f"   ❌ {service_name}: Connection failed ({e})")

async def test_gateway_routing():
    """API Gateway 라우팅 테스트"""
    print("\n🔄 Testing API Gateway routing...")
    
    async with httpx.AsyncClient() as client:
        # Gateway 기본 엔드포인트
        try:
            response = await client.get(f"{BASE_URL}/")
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Gateway root: {data['message']}")
            else:
                print(f"   ❌ Gateway root failed: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Gateway root error: {e}")
        
        # Health check through gateway
        try:
            response = await client.get(f"{BASE_URL}/health")
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Gateway health check passed")
                print(f"       Services status: {data.get('services', {})}")
            else:
                print(f"   ❌ Gateway health check failed: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Gateway health check error: {e}")

async def test_ai_image_service():
    """AI Image Service 테스트"""
    print("\n🎨 Testing AI Image Service...")
    
    async with httpx.AsyncClient() as client:
        # 이미지 생성 요청
        try:
            payload = {
                "prompt": "A beautiful sunset over mountains",
                "style": "realistic",
                "width": 512,
                "height": 512,
                "count": 1
            }
            
            response = await client.post(
                f"{BASE_URL}/api/v1/ai/image/generate",
                json=payload,
                timeout=10.0
            )
            
            if response.status_code == 200:
                data = response.json()
                generation_id = data.get('id')
                print(f"   ✅ Image generation started: {generation_id}")
                
                # 상태 확인
                await asyncio.sleep(2)
                status_response = await client.get(
                    f"{BASE_URL}/api/v1/ai/image/status/{generation_id}"
                )
                
                if status_response.status_code == 200:
                    status_data = status_response.json()
                    print(f"   ✅ Generation status: {status_data.get('status')}")
                else:
                    print(f"   ❌ Status check failed: {status_response.status_code}")
                    
            else:
                print(f"   ❌ Image generation failed: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ AI Image Service error: {e}")

async def test_excel_automation():
    """Excel Automation Service 테스트"""
    print("\n📊 Testing Excel Automation Service...")
    
    async with httpx.AsyncClient() as client:
        try:
            # 모의 엑셀 파일 생성
            import io
            import pandas as pd
            
            # 테스트 데이터 생성
            test_data = pd.DataFrame({
                'Name': ['Alice', 'Bob', 'Charlie'],
                'Age': [25, 30, 35],
                'City': ['New York', 'London', 'Tokyo']
            })
            
            # 바이트 스트림으로 변환
            excel_buffer = io.BytesIO()
            test_data.to_excel(excel_buffer, index=False)
            excel_buffer.seek(0)
            
            # 파일 업로드 및 분석 요청
            files = {"file": ("test.xlsx", excel_buffer.getvalue(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
            
            response = await client.post(
                f"{BASE_URL}/api/v1/automation/excel/analyze",
                files=files,
                timeout=10.0
            )
            
            if response.status_code == 200:
                data = response.json()
                job_id = data.get('job_id')
                print(f"   ✅ Excel analysis started: {job_id}")
                
                # 상태 확인
                await asyncio.sleep(3)
                status_response = await client.get(
                    f"{BASE_URL}/api/v1/automation/excel/status/{job_id}"
                )
                
                if status_response.status_code == 200:
                    status_data = status_response.json()
                    print(f"   ✅ Analysis status: {status_data.get('status')}")
                    if status_data.get('result'):
                        result = status_data['result']
                        print(f"       Rows: {result.get('total_rows')}, Columns: {result.get('total_columns')}")
                else:
                    print(f"   ❌ Status check failed: {status_response.status_code}")
                    
            else:
                print(f"   ❌ Excel analysis failed: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Excel Automation Service error: {e}")

async def main():
    """메인 테스트 실행"""
    print("🧪 Smart Person AI - Service Testing")
    print("=" * 50)
    
    await test_service_health()
    await test_gateway_routing()
    await test_ai_image_service()
    await test_excel_automation()
    
    print("\n✅ Testing completed!")

if __name__ == "__main__":
    asyncio.run(main())