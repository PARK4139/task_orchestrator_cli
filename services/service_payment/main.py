"""
Payment Service

결제 및 구독 관리 서비스
포트: 8021
"""

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List, Dict
import structlog
from datetime import datetime, timedelta
import uuid

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from shared.config import settings

logger = structlog.get_logger()

app = FastAPI(
    title="Smart Person AI - Payment Service",
    description="결제 및 구독 관리 서비스",
    version="0.1.0"
)

# 요청/응답 모델
class SubscriptionPlan(BaseModel):
    name: str
    price: int  # 원 단위
    tokens: int  # 월 토큰 수
    features: List[str]

class UserSubscription(BaseModel):
    user_id: str
    plan_name: str
    tokens_used: int
    tokens_remaining: int
    start_date: datetime
    end_date: datetime
    status: str  # active, expired, cancelled

class PaymentRequest(BaseModel):
    user_id: str
    plan_name: str
    payment_method: str  # card, transfer, paypal

class TokenUsageRequest(BaseModel):
    user_id: str
    service: str  # ai_image, ai_book, excel_automation, web_crawler
    tokens_consumed: int

# 구독 플랜 정의
SUBSCRIPTION_PLANS = {
    "basic": SubscriptionPlan(
        name="베이직",
        price=9900,
        tokens=100,
        features=["AI 이미지 생성", "기본 엑셀 자동화", "이메일 지원"]
    ),
    "premium": SubscriptionPlan(
        name="프리미엄",
        price=19900,
        tokens=500,
        features=["모든 베이직 기능", "AI 동화책 생성", "웹 크롤링", "우선 지원"]
    ),
    "pro": SubscriptionPlan(
        name="프로",
        price=49900,
        tokens=2000,
        features=["모든 프리미엄 기능", "커스텀 파이프라인", "전화 지원", "SLA 보장"]
    )
}

# 임시 저장소 (실제로는 데이터베이스 사용)
user_subscriptions = {}
payment_history = {}

@app.get("/")
async def root():
    """서비스 상태 확인"""
    return {
        "service": "Payment Service", 
        "status": "running",
        "port": settings.payment_service_port
    }

@app.get("/health")
async def health_check():
    """헬스체크"""
    return {"status": "healthy", "service": "payment"}

@app.get("/api/v1/plans")
async def get_subscription_plans():
    """구독 플랜 목록 조회"""
    return {
        "plans": list(SUBSCRIPTION_PLANS.values()),
        "currency": "KRW"
    }

@app.get("/api/v1/subscription/{user_id}")
async def get_user_subscription(user_id: str):
    """사용자 구독 정보 조회"""
    
    if user_id not in user_subscriptions:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    return user_subscriptions[user_id]

@app.post("/api/v1/subscribe")
async def create_subscription(request: PaymentRequest):
    """구독 생성 (결제 처리)"""
    
    if request.plan_name not in SUBSCRIPTION_PLANS:
        raise HTTPException(status_code=400, detail="Invalid subscription plan")
    
    plan = SUBSCRIPTION_PLANS[request.plan_name]
    
    # TODO: 실제 결제 처리 (토스페이먼츠, 아임포트 등)
    payment_id = str(uuid.uuid4())
    
    # 구독 정보 생성
    subscription = UserSubscription(
        user_id=request.user_id,
        plan_name=plan.name,
        tokens_used=0,
        tokens_remaining=plan.tokens,
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(days=30),
        status="active"
    )
    
    user_subscriptions[request.user_id] = subscription
    
    # 결제 기록 저장
    payment_history[payment_id] = {
        "payment_id": payment_id,
        "user_id": request.user_id,
        "amount": plan.price,
        "plan_name": plan.name,
        "payment_method": request.payment_method,
        "status": "completed",
        "created_at": datetime.now()
    }
    
    logger.info("Subscription created", user_id=request.user_id, plan=plan.name)
    
    return {
        "status": "success",
        "payment_id": payment_id,
        "subscription": subscription
    }

@app.post("/api/v1/tokens/consume")
async def consume_tokens(request: TokenUsageRequest):
    """토큰 사용량 차감"""
    
    if request.user_id not in user_subscriptions:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    subscription = user_subscriptions[request.user_id]
    
    # 토큰 부족 체크
    if subscription.tokens_remaining < request.tokens_consumed:
        raise HTTPException(
            status_code=402, 
            detail="Insufficient tokens. Please upgrade your plan."
        )
    
    # 토큰 차감
    subscription.tokens_used += request.tokens_consumed
    subscription.tokens_remaining -= request.tokens_consumed
    
    logger.info("Tokens consumed", 
                user_id=request.user_id,
                service=request.service,
                tokens=request.tokens_consumed)
    
    return {
        "status": "success",
        "tokens_remaining": subscription.tokens_remaining,
        "service_used": request.service
    }

@app.get("/api/v1/usage/{user_id}")
async def get_token_usage(user_id: str):
    """사용자 토큰 사용량 조회"""
    
    if user_id not in user_subscriptions:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    subscription = user_subscriptions[user_id]
    plan = SUBSCRIPTION_PLANS.get(subscription.plan_name.lower(), SUBSCRIPTION_PLANS["basic"])
    
    usage_percentage = (subscription.tokens_used / plan.tokens) * 100
    
    return {
        "user_id": user_id,
        "plan": subscription.plan_name,
        "tokens_total": plan.tokens,
        "tokens_used": subscription.tokens_used,
        "tokens_remaining": subscription.tokens_remaining,
        "usage_percentage": round(usage_percentage, 2),
        "days_remaining": (subscription.end_date - datetime.now()).days
    }

@app.post("/api/v1/cancel/{user_id}")
async def cancel_subscription(user_id: str):
    """구독 취소"""
    
    if user_id not in user_subscriptions:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    subscription = user_subscriptions[user_id]
    subscription.status = "cancelled"
    
    logger.info("Subscription cancelled", user_id=user_id)
    
    return {
        "status": "success",
        "message": "Subscription cancelled successfully"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.payment_service_port,
        reload=settings.debug
    )