"""
Middleware application module for API Gateway.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from typing import List

def ensure_middleware_applied(app: FastAPI, cors_origins: List[str] = None, trusted_hosts: List[str] = None):
    """
    FastAPI 애플리케이션에 미들웨어를 확실히 적용합니다.
    """
    if cors_origins is None:
        cors_origins = ["*"]
    
    if trusted_hosts is None:
        trusted_hosts = ["*"]
    
    # CORS 미들웨어 적용
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Trusted Host 미들웨어 적용
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=trusted_hosts
    ) 