"""
Logging configuration for the finance investment assistant project.
"""
import logging
import sys
from pathlib import Path
from .config import settings


def ensure_logging_configured():
    """Ensure logging is properly configured."""
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL),
        format=settings.LOG_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_dir / "finance_assistant.log")
        ]
    )
    
    # Set specific logger levels
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("sqlalchemy").setLevel(logging.WARNING)
    
    return logging.getLogger(__name__)


def get_logger(name: str) -> logging.Logger:
    """Get logger instance with the specified name."""
    return logging.getLogger(name)


# Initialize logging
logger = ensure_logging_configured() 