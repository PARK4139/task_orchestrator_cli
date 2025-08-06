"""
AI Book Service

Claude를 활용한 동화책 생성 서비스
포트: 8002
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Optional, List
import structlog
from datetime import datetime
import uuid

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from shared.config import settings

logger = structlog.get_logger()

app = FastAPI(
    title="Smart Person AI - Book Service",
    description="AI 동화책 생성 서비스",
    version="0.1.0"
)

# 요청 모델
class BookGenerationRequest(BaseModel):
    title: Optional[str] = None
    theme: str  # fantasy, education, adventure, moral
    target_age: Optional[int] = 5  # 5-12세
    pages: Optional[int] = 10
    language: Optional[str] = "korean"
    
class BookResponse(BaseModel):
    id: str
    title: str
    theme: str
    status: str  # pending, processing, completed, failed
    created_at: datetime
    pages_content: Optional[List[str]] = None
    error: Optional[str] = None

# 임시 저장소
book_generations = {}

@app.get("/")
async def root():
    """서비스 상태 확인"""
    return {
        "service": "AI Book Service",
        "status": "running",
        "port": settings.ai_book_service_port
    }

@app.get("/health")
async def health_check():
    """헬스체크"""
    return {"status": "healthy", "service": "ai_book"}

@app.post("/api/v1/generate", response_model=BookResponse)
async def generate_book(
    request: BookGenerationRequest,
    background_tasks: BackgroundTasks
):
    """AI 동화책 생성 요청"""
    
    generation_id = str(uuid.uuid4())
    title = request.title or f"Magic Story for Age {request.target_age}"
    
    book_response = BookResponse(
        id=generation_id,
        title=title,
        theme=request.theme,
        status="pending",
        created_at=datetime.now()
    )
    
    book_generations[generation_id] = book_response
    
    # 백그라운드에서 동화책 생성 처리
    background_tasks.add_task(
        _process_book_generation,
        generation_id,
        request
    )
    
    logger.info("Book generation requested", 
                generation_id=generation_id, 
                theme=request.theme)
    
    return book_response

@app.get("/api/v1/status/{generation_id}", response_model=BookResponse)
async def get_generation_status(generation_id: str):
    """동화책 생성 상태 조회"""
    
    if generation_id not in book_generations:
        raise HTTPException(status_code=404, detail="Generation not found")
    
    return book_generations[generation_id]

async def _process_book_generation(generation_id: str, request: BookGenerationRequest):
    """실제 동화책 생성 처리 (백그라운드 작업)"""
    
    try:
        import asyncio
        
        book_generations[generation_id].status = "processing"
        
        logger.info("Starting book generation", generation_id=generation_id)
        
        # TODO: 실제 Claude API 호출
        # 현재는 모의 처리
        await asyncio.sleep(15)  # 동화책 생성 시뮬레이션
        
        # 모의 동화책 페이지들
        mock_pages = [
            f"Once upon a time, there was a magical {request.theme} story...",
            f"The adventure began when our hero discovered something amazing...",
            f"Through challenges and friendship, they learned valuable lessons...",
            f"And they all lived happily ever after! The End."
        ]
        
        book_generations[generation_id].status = "completed"
        book_generations[generation_id].pages_content = mock_pages
        
        logger.info("Book generation completed", 
                   generation_id=generation_id,
                   pages_count=len(mock_pages))
        
    except Exception as e:
        book_generations[generation_id].status = "failed"
        book_generations[generation_id].error = str(e)
        
        logger.error("Book generation failed", 
                    generation_id=generation_id,
                    error=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.ai_book_service_port,
        reload=settings.debug
    )