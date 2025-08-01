"""
Exception handling module for API Gateway.
"""
from fastapi import HTTPException
from typing import Any, Dict
import httpx
import logging

logger = logging.getLogger(__name__)

class GatewayException(Exception):
    """API Gateway 커스텀 예외 클래스."""
    
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

def ensure_exceptions_handled(func):
    """
    함수 실행 중 발생하는 예외를 확실히 처리하는 데코레이터.
    """
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except httpx.RequestError as e:
            logger.error(f"HTTP request error: {e}")
            raise HTTPException(
                status_code=503, 
                detail="Service temporarily unavailable"
            )
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP status error: {e}")
            raise HTTPException(
                status_code=e.response.status_code,
                detail=f"Upstream service error: {e.response.text}"
            )
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise HTTPException(
                status_code=500,
                detail="Internal server error"
            )
    
    return wrapper

def ensure_service_response_valid(response: httpx.Response) -> Dict[str, Any]:
    """
    서비스 응답이 유효한지 확실히 확인합니다.
    """
    try:
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Invalid service response: {e}")
        raise GatewayException(
            f"Service returned error: {e.response.status_code}",
            status_code=e.response.status_code
        )
    except Exception as e:
        logger.error(f"Failed to parse service response: {e}")
        raise GatewayException("Invalid service response format") 