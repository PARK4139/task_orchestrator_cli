"""
Official Home Backend Service

현사AI 공식 홈페이지 백엔드 API
포트: 8030
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Optional, List
import structlog
from datetime import datetime
import uuid

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from shared.config import settings

logger = structlog.get_logger()

app = FastAPI(
    title="현사AI - Official Home Backend",
    description="공식 홈페이지 백엔드 API",
    version="0.1.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://smartpersonai.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청/응답 모델
class ContactRequest(BaseModel):
    name: str
    email: EmailStr
    company: Optional[str] = None
    message: str
    service_interest: Optional[List[str]] = []  # ai_image, ai_book, excel_automation, etc.

class NewsletterRequest(BaseModel):
    email: EmailStr
    interests: Optional[List[str]] = []

class DemoRequest(BaseModel):
    name: str
    email: EmailStr
    company: Optional[str] = None
    preferred_time: Optional[str] = None
    service_interest: str

# 임시 저장소 (실제로는 데이터베이스 사용)
contacts = {}
newsletters = {}
demo_requests = {}

@app.get("/")
async def root():
    """서비스 상태 확인"""
    return {
        "service": "Official Home Backend",
        "status": "running",
        "port": 8030,
        "description": "현사AI 공식 홈페이지 백엔드"
    }

@app.get("/health")
async def health_check():
    """헬스체크"""
    return {"status": "healthy", "service": "official_home_backend"}

@app.post("/api/v1/contact")
async def submit_contact(
    request: ContactRequest,
    background_tasks: BackgroundTasks
):
    """문의 접수"""
    
    contact_id = str(uuid.uuid4())
    
    contact_data = {
        "id": contact_id,
        "name": request.name,
        "email": request.email,
        "company": request.company,
        "message": request.message,
        "service_interest": request.service_interest,
        "submitted_at": datetime.now(),
        "status": "new"
    }
    
    contacts[contact_id] = contact_data
    
    # 백그라운드에서 이메일 발송
    background_tasks.add_task(
        _send_contact_notification,
        contact_data
    )
    
    logger.info("Contact form submitted", 
                contact_id=contact_id, 
                email=request.email)
    
    return {
        "status": "success",
        "message": "문의가 성공적으로 접수되었습니다. 빠른 시일 내에 연락드리겠습니다.",
        "contact_id": contact_id
    }

@app.post("/api/v1/newsletter")
async def subscribe_newsletter(
    request: NewsletterRequest,
    background_tasks: BackgroundTasks
):
    """뉴스레터 구독"""
    
    subscription_id = str(uuid.uuid4())
    
    # 중복 구독 체크
    existing = next((s for s in newsletters.values() if s["email"] == request.email), None)
    if existing:
        return {
            "status": "info",
            "message": "이미 구독하신 이메일입니다.",
            "subscription_id": existing["id"]
        }
    
    subscription_data = {
        "id": subscription_id,
        "email": request.email,
        "interests": request.interests,
        "subscribed_at": datetime.now(),
        "status": "active"
    }
    
    newsletters[subscription_id] = subscription_data
    
    # 백그라운드에서 환영 이메일 발송
    background_tasks.add_task(
        _send_welcome_email,
        subscription_data
    )
    
    logger.info("Newsletter subscription", 
                subscription_id=subscription_id, 
                email=request.email)
    
    return {
        "status": "success",
        "message": "뉴스레터 구독이 완료되었습니다. 환영 이메일을 확인해주세요!",
        "subscription_id": subscription_id
    }

@app.post("/api/v1/demo-request")
async def request_demo(
    request: DemoRequest,
    background_tasks: BackgroundTasks
):
    """데모 요청"""
    
    demo_id = str(uuid.uuid4())
    
    demo_data = {
        "id": demo_id,
        "name": request.name,
        "email": request.email,
        "company": request.company,
        "preferred_time": request.preferred_time,
        "service_interest": request.service_interest,
        "requested_at": datetime.now(),
        "status": "pending"
    }
    
    demo_requests[demo_id] = demo_data
    
    # 백그라운드에서 데모 스케줄링
    background_tasks.add_task(
        _schedule_demo,
        demo_data
    )
    
    logger.info("Demo requested", 
                demo_id=demo_id, 
                email=request.email,
                service=request.service_interest)
    
    return {
        "status": "success",
        "message": "데모 요청이 접수되었습니다. 담당자가 연락드려 일정을 조율하겠습니다.",
        "demo_id": demo_id
    }

@app.get("/api/v1/services-overview")
async def get_services_overview():
    """서비스 개요 정보 제공 (홈페이지용)"""
    
    services_data = {
        "services": [
            {
                "id": "ai_image",
                "name": "AI 이미지 생성",
                "description": "Stable Diffusion으로 고품질 이미지를 생성하세요",
                "icon": "🎨",
                "features": ["다양한 스타일", "고화질 생성", "빠른 처리"],
                "pricing": "베이직부터 사용 가능"
            },
            {
                "id": "ai_book",
                "name": "AI 동화책 생성",
                "description": "Claude AI로 창의적인 동화책을 만들어보세요",
                "icon": "📚",
                "features": ["맞춤형 스토리", "연령별 최적화", "교육 콘텐츠"],
                "pricing": "프리미엄부터 사용 가능"
            },
            {
                "id": "excel_automation",
                "name": "엑셀 자동화",
                "description": "복잡한 엑셀 작업을 자동으로 처리합니다",
                "icon": "📊",
                "features": ["파일 병합", "데이터 분석", "차트 생성"],
                "pricing": "베이직부터 사용 가능"
            },
            {
                "id": "web_crawler",
                "name": "웹 크롤링",
                "description": "주가, 뉴스 등 웹 데이터를 자동 수집합니다",
                "icon": "🕷️",
                "features": ["실시간 수집", "감정 분석", "데이터 정제"],
                "pricing": "프리미엄부터 사용 가능"
            }
        ],
        "pricing_plans": [
            {
                "name": "베이직",
                "price": 9900,
                "tokens": 100,
                "features": ["AI 이미지 생성", "기본 엑셀 자동화", "이메일 지원"]
            },
            {
                "name": "프리미엄",
                "price": 19900,
                "tokens": 500,
                "features": ["모든 베이직 기능", "AI 동화책 생성", "웹 크롤링", "우선 지원"]
            },
            {
                "name": "프로",
                "price": 49900,
                "tokens": 2000,
                "features": ["모든 프리미엄 기능", "커스텀 파이프라인", "전화 지원", "SLA 보장"]
            }
        ]
    }
    
    return services_data

@app.get("/api/v1/testimonials")
async def get_testimonials():
    """고객 후기 (홈페이지용)"""
    
    testimonials = [
        {
            "name": "김○○ 대표",
            "company": "○○ 스타트업",
            "service": "AI 이미지 생성",
            "content": "마케팅 이미지 제작 시간이 90% 단축되었습니다. 정말 혁신적이에요!",
            "rating": 5
        },
        {
            "name": "박○○ 팀장",
            "company": "○○ 기획사",
            "service": "엑셀 자동화",
            "content": "매월 3일 걸리던 보고서 작업이 30분으로 줄었습니다.",
            "rating": 5
        },
        {
            "name": "이○○ 선생님",
            "company": "○○ 어린이집",
            "service": "AI 동화책",
            "content": "아이들이 정말 좋아해요. 매일 새로운 동화책을 만들어줄 수 있어서 좋습니다.",
            "rating": 5
        }
    ]
    
    return {"testimonials": testimonials}

async def _send_contact_notification(contact_data: dict):
    """문의 알림 이메일 발송 (백그라운드 작업)"""
    # TODO: 실제 이메일 발송 구현
    logger.info("Contact notification sent", contact_id=contact_data["id"])

async def _send_welcome_email(subscription_data: dict):
    """뉴스레터 환영 이메일 발송 (백그라운드 작업)"""
    # TODO: 실제 이메일 발송 구현  
    logger.info("Welcome email sent", subscription_id=subscription_data["id"])

async def _schedule_demo(demo_data: dict):
    """데모 스케줄링 (백그라운드 작업)"""
    # TODO: 캘린더 연동 및 스케줄링 구현
    logger.info("Demo scheduled", demo_id=demo_data["id"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8030,
        reload=settings.debug
    )