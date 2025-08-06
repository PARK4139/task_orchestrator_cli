"""
Smart Person AI - API Gateway

모든 마이크로서비스의 중앙 진입점
- 라우팅
- 인증/인가
- Rate Limiting  
- 로깅
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import httpx
import structlog
from shared.config import settings

# 구조화된 로깅 설정
logger = structlog.get_logger()

app = FastAPI(
    title="Smart Person AI Gateway",
    description="현명한 사람들의 AI - API Gateway",
    version=settings.app_version,
    debug=settings.debug
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영에서는 특정 도메인만 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 서비스 엔드포인트 매핑
SERVICE_URLS = {
    "ai_image": f"http://localhost:{settings.ai_image_service_port}",
    "ai_book": f"http://localhost:{settings.ai_book_service_port}",
    "excel_automation": f"http://localhost:{settings.excel_automation_port}",  
    "web_crawler": f"http://localhost:{settings.web_crawler_port}",
    "payment": f"http://localhost:{settings.payment_service_port}",
}

@app.get("/")
async def root():
    """API Gateway 상태 확인"""
    return {
        "message": "Smart Person AI Gateway",
        "version": settings.app_version,
        "status": "running",
        "services": list(SERVICE_URLS.keys())
    }

@app.get("/health")
async def health_check():
    """헬스체크 엔드포인트"""
    service_status = {}
    
    async with httpx.AsyncClient() as client:
        for service_name, service_url in SERVICE_URLS.items():
            try:
                response = await client.get(f"{service_url}/health", timeout=5.0)
                service_status[service_name] = {
                    "status": "healthy" if response.status_code == 200 else "unhealthy",
                    "response_time": response.elapsed.total_seconds()
                }
            except Exception as e:
                service_status[service_name] = {
                    "status": "unhealthy", 
                    "error": str(e)
                }
    
    return {
        "gateway": "healthy",
        "services": service_status
    }

# AI Content Domain 라우팅
@app.api_route("/api/v1/ai/image/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_ai_image(path: str, request):
    """AI Image Service로 프록시"""
    return await _proxy_request("ai_image", f"/api/v1/{path}", request)

@app.api_route("/api/v1/ai/book/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])  
async def proxy_ai_book(path: str, request):
    """AI Book Service로 프록시"""
    return await _proxy_request("ai_book", f"/api/v1/{path}", request)

# Automation Domain 라우팅
@app.api_route("/api/v1/automation/excel/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_excel_automation(path: str, request):
    """Excel Automation Service로 프록시"""
    return await _proxy_request("excel_automation", f"/api/v1/{path}", request)

@app.api_route("/api/v1/automation/crawler/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_web_crawler(path: str, request):
    """Web Crawler Service로 프록시"""
    return await _proxy_request("web_crawler", f"/api/v1/{path}", request)

# Business Domain 라우팅  
@app.api_route("/api/v1/payment/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_payment(path: str, request):
    """Payment Service로 프록시"""
    return await _proxy_request("payment", f"/api/v1/{path}", request)

async def _proxy_request(service_name: str, path: str, request):
    """내부 서비스로 요청 프록시"""
    service_url = SERVICE_URLS.get(service_name)
    if not service_url:
        raise HTTPException(status_code=404, detail=f"Service {service_name} not found")
    
    url = f"{service_url}{path}"
    
    # 요청 로깅
    logger.info("Proxying request", service=service_name, path=path, method=request.method)
    
    async with httpx.AsyncClient() as client:
        try:
            # 원본 요청의 모든 정보를 전달
            response = await client.request(
                method=request.method,
                url=url,
                params=request.query_params,
                headers=dict(request.headers),
                content=await request.body(),
                timeout=30.0
            )
            
            return response.json() if response.headers.get("content-type", "").startswith("application/json") else response.text
            
        except httpx.TimeoutException:
            logger.error("Service timeout", service=service_name, url=url)
            raise HTTPException(status_code=504, detail=f"Service {service_name} timeout")
        except httpx.RequestError as e:
            logger.error("Service request error", service=service_name, error=str(e))
            raise HTTPException(status_code=502, detail=f"Service {service_name} unavailable")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api_gateway:app",
        host="0.0.0.0", 
        port=settings.api_gateway_port,
        reload=settings.debug
    )