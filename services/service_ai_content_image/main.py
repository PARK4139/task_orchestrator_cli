"""
AI Image Service

Stable Diffusion을 활용한 이미지 생성 서비스
포트: 8001
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Optional, List
import httpx
import asyncio
import structlog
from datetime import datetime
import uuid

from shared.config import settings
from shared.database import get_db, get_redis

logger = structlog.get_logger()

app = FastAPI(
    title="Smart Person AI - Image Service",
    description="AI 이미지 생성 서비스",
    version="0.1.0"
)

# 요청 모델
class ImageGenerationRequest(BaseModel):
    prompt: str
    style: Optional[str] = "realistic"  # realistic, anime, cartoon, artistic
    width: Optional[int] = 512
    height: Optional[int] = 512
    count: Optional[int] = 1
    
class ImageResponse(BaseModel):
    id: str
    prompt: str
    style: str
    status: str  # pending, processing, completed, failed
    created_at: datetime
    image_urls: Optional[List[str]] = None
    error: Optional[str] = None

# 임시 메모리 저장소 (실제로는 데이터베이스 사용)
image_generations = {}

@app.get("/")
async def root():
    """서비스 상태 확인"""
    return {
        "service": "AI Image Service",
        "status": "running",
        "port": settings.ai_image_service_port
    }

@app.get("/health")
async def health_check():
    """헬스체크"""
    return {"status": "healthy", "service": "ai_image"}

@app.post("/api/v1/generate", response_model=ImageResponse)
async def generate_image(
    request: ImageGenerationRequest,
    background_tasks: BackgroundTasks
):
    """AI 이미지 생성 요청"""
    
    # 요청 ID 생성
    generation_id = str(uuid.uuid4())
    
    # 요청 정보 저장
    image_response = ImageResponse(
        id=generation_id,
        prompt=request.prompt,
        style=request.style,
        status="pending",
        created_at=datetime.now()
    )
    
    image_generations[generation_id] = image_response
    
    # 백그라운드에서 이미지 생성 처리
    background_tasks.add_task(
        _process_image_generation,
        generation_id,
        request
    )
    
    logger.info("Image generation requested", 
                generation_id=generation_id, 
                prompt=request.prompt)
    
    return image_response

@app.get("/api/v1/status/{generation_id}", response_model=ImageResponse)
async def get_generation_status(generation_id: str):
    """이미지 생성 상태 조회"""
    
    if generation_id not in image_generations:
        raise HTTPException(status_code=404, detail="Generation not found")
    
    return image_generations[generation_id]

@app.get("/api/v1/history")
async def get_generation_history(limit: int = 10):
    """이미지 생성 히스토리 조회"""
    
    generations = list(image_generations.values())
    # 최신순 정렬
    generations.sort(key=lambda x: x.created_at, reverse=True)
    
    return {
        "generations": generations[:limit],
        "total": len(generations)
    }

async def _process_image_generation(generation_id: str, request: ImageGenerationRequest):
    """실제 이미지 생성 처리 (백그라운드 작업)"""
    
    try:
        # 상태를 processing으로 변경
        image_generations[generation_id].status = "processing"
        
        logger.info("Starting image generation", generation_id=generation_id)
        
        # TODO: 실제 Stable Diffusion API 호출
        # 현재는 모의 처리
        await asyncio.sleep(10)  # 이미지 생성 시뮬레이션
        
        # 모의 이미지 URL들
        mock_image_urls = [
            f"https://example.com/images/{generation_id}_{i}.png"
            for i in range(request.count)
        ]
        
        # 완료 상태로 업데이트
        image_generations[generation_id].status = "completed"
        image_generations[generation_id].image_urls = mock_image_urls
        
        logger.info("Image generation completed", 
                   generation_id=generation_id,
                   image_count=len(mock_image_urls))
        
    except Exception as e:
        # 실패 상태로 업데이트
        image_generations[generation_id].status = "failed"
        image_generations[generation_id].error = str(e)
        
        logger.error("Image generation failed", 
                    generation_id=generation_id,
                    error=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.ai_image_service_port,
        reload=settings.debug
    )