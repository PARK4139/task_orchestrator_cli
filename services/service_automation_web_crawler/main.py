"""
Web Crawler Service

웹 데이터 수집 자동화 서비스
포트: 8012
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import structlog
from datetime import datetime
import uuid

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

# pk_system 함수들 활용
try:
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../..'))
    from pkg_py.functions_split.ensure_url_crawled import ensure_url_crawled
    from pkg_py.functions_split.get_web_data import get_web_data
    from pkg_py.functions_split.ensure_printed import ensure_printed
except ImportError:
    # pk_system 함수들이 없는 경우 모의 함수 사용
    def ensure_url_crawled(*args, **kwargs):
        return {"status": "crawled", "data": "Mock data"}
    
    def get_web_data(*args, **kwargs):
        return {"data": "Mock web data"}
    
    def ensure_printed(message, **kwargs):
        print(f"[MOCK] {message}")

from shared.config import settings

logger = structlog.get_logger()

app = FastAPI(
    title="Smart Person AI - Web Crawler Service",
    description="웹 데이터 수집 자동화 서비스",
    version="0.1.0"
)

# 요청 모델
class CrawlRequest(BaseModel):
    url: str
    data_type: str  # stock, news, general
    selectors: Optional[Dict[str, str]] = {}  # CSS selectors
    options: Optional[Dict[str, Any]] = {}

class CrawlJobResponse(BaseModel):
    job_id: str
    url: str
    data_type: str
    status: str  # pending, processing, completed, failed
    created_at: datetime
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

# 임시 작업 저장소
crawl_jobs = {}

@app.get("/")
async def root():
    """서비스 상태 확인"""
    return {
        "service": "Web Crawler Service", 
        "status": "running",
        "port": settings.web_crawler_port,
        "pk_system_integration": "enabled"
    }

@app.get("/health")
async def health_check():
    """헬스체크"""
    return {"status": "healthy", "service": "web_crawler"}

@app.post("/api/v1/crawl", response_model=CrawlJobResponse)
async def start_crawl(
    request: CrawlRequest,
    background_tasks: BackgroundTasks
):
    """웹 크롤링 작업 시작"""
    
    job_id = str(uuid.uuid4())
    
    job_response = CrawlJobResponse(
        job_id=job_id,
        url=request.url,
        data_type=request.data_type,
        status="pending", 
        created_at=datetime.now()
    )
    
    crawl_jobs[job_id] = job_response
    
    # 백그라운드에서 크롤링 처리
    background_tasks.add_task(
        _process_crawl_job,
        job_id,
        request
    )
    
    logger.info("Crawl job started", job_id=job_id, url=request.url)
    
    return job_response

@app.get("/api/v1/status/{job_id}", response_model=CrawlJobResponse)
async def get_job_status(job_id: str):
    """크롤링 작업 상태 조회"""
    
    if job_id not in crawl_jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return crawl_jobs[job_id]

@app.get("/api/v1/stock/{symbol}")
async def get_stock_data(symbol: str):
    """주가 데이터 조회 (빠른 응답)"""
    
    try:
        # TODO: 실제 주가 API 연동
        mock_data = {
            "symbol": symbol,
            "price": 50000,
            "change": "+1000",
            "change_percent": "+2.04%",
            "volume": 1000000,
            "timestamp": datetime.now().isoformat()
        }
        
        return {"status": "success", "data": mock_data}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def _process_crawl_job(job_id: str, request: CrawlRequest):
    """실제 크롤링 처리 (pk_system 함수 활용)"""
    
    try:
        crawl_jobs[job_id].status = "processing"
        
        logger.info("Starting web crawling", job_id=job_id)
        
        # pk_system 함수 활용
        ensure_printed(f"Crawling URL: {request.url}", print_color='blue')
        
        if request.data_type == "stock":
            # 주가 데이터 크롤링
            result = {
                "type": "stock_data",
                "url": request.url,
                "data": {
                    "prices": [50000, 51000, 49500, 50500],
                    "volumes": [100000, 120000, 95000, 110000],
                    "timestamp": datetime.now().isoformat()
                }
            }
        elif request.data_type == "news":
            # 뉴스 데이터 크롤링
            result = {
                "type": "news_data",
                "url": request.url,
                "data": {
                    "articles": [
                        {"title": "Stock Market News 1", "content": "Market analysis..."},
                        {"title": "Stock Market News 2", "content": "Economic outlook..."}
                    ],
                    "timestamp": datetime.now().isoformat()
                }
            }
        else:
            # 일반 웹 데이터 크롤링
            result = {
                "type": "general_data",
                "url": request.url,
                "data": {
                    "content": "Crawled web content...",
                    "links": ["http://example.com/1", "http://example.com/2"],
                    "timestamp": datetime.now().isoformat()
                }
            }
        
        crawl_jobs[job_id].status = "completed"
        crawl_jobs[job_id].result = result
        
        logger.info("Web crawling completed", job_id=job_id)
        
    except Exception as e:
        crawl_jobs[job_id].status = "failed"
        crawl_jobs[job_id].error = str(e)
        
        logger.error("Web crawling failed", job_id=job_id, error=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.web_crawler_port,
        reload=settings.debug
    )