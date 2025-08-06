"""
Excel Automation Service

엑셀 파일 처리 자동화 서비스
포트: 8011

기존 pk_system의 함수들을 활용하여 엑셀 자동화 기능 제공
"""

from fastapi import FastAPI, HTTPException, UploadFile, File, BackgroundTasks
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import pandas as pd
import openpyxl
from io import BytesIO
import uuid
from datetime import datetime
import structlog

# pk_system 함수들 import (절대 경로 사용)
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../..'))

# 기존 pk_system 함수들 활용
try:
    from pkg_py.functions_split.ensure_xlsx_processed import ensure_xlsx_processed
    from pkg_py.functions_split.get_xlsx_data import get_xlsx_data
    from pkg_py.functions_split.ensure_printed import ensure_printed
except ImportError:
    # pk_system 함수들이 없는 경우 모의 함수 사용
    def ensure_xlsx_processed(*args, **kwargs):
        return {"status": "processed", "message": "Mock function"}
    
    def get_xlsx_data(*args, **kwargs):
        return {"data": "Mock data"}
    
    def ensure_printed(message, **kwargs):
        print(f"[MOCK] {message}")

from shared.config import settings

logger = structlog.get_logger()

app = FastAPI(
    title="Smart Person AI - Excel Automation Service",
    description="엑셀 파일 자동화 처리 서비스",
    version="0.1.0"
)

# 요청 모델
class ExcelMergeRequest(BaseModel):
    operation: str  # merge, split, analyze, convert
    options: Optional[Dict[str, Any]] = {}

class ExcelJobResponse(BaseModel):
    job_id: str
    operation: str
    status: str  # pending, processing, completed, failed
    created_at: datetime
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

# 임시 작업 저장소
excel_jobs = {}

@app.get("/")
async def root():
    """서비스 상태 확인"""
    return {
        "service": "Excel Automation Service", 
        "status": "running",
        "port": settings.excel_automation_port,
        "pk_system_integration": "enabled"
    }

@app.get("/health")
async def health_check():
    """헬스체크"""
    return {"status": "healthy", "service": "excel_automation"}

@app.post("/api/v1/merge", response_model=ExcelJobResponse)
async def merge_excel_files(
    files: List[UploadFile] = File(...),
    background_tasks: BackgroundTasks = None
):
    """엑셀 파일 병합"""
    
    job_id = str(uuid.uuid4())
    
    # 작업 정보 저장
    job_response = ExcelJobResponse(
        job_id=job_id,
        operation="merge",
        status="pending", 
        created_at=datetime.now()
    )
    
    excel_jobs[job_id] = job_response
    
    # 백그라운드에서 병합 처리
    background_tasks.add_task(
        _process_excel_merge,
        job_id,
        files
    )
    
    logger.info("Excel merge job started", job_id=job_id, file_count=len(files))
    
    return job_response

@app.post("/api/v1/analyze", response_model=ExcelJobResponse)  
async def analyze_excel_file(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = None
):
    """엑셀 파일 분석"""
    
    job_id = str(uuid.uuid4())
    
    job_response = ExcelJobResponse(
        job_id=job_id,
        operation="analyze",
        status="pending",
        created_at=datetime.now()
    )
    
    excel_jobs[job_id] = job_response
    
    # 백그라운드에서 분석 처리
    background_tasks.add_task(
        _process_excel_analysis,
        job_id,
        file
    )
    
    logger.info("Excel analysis job started", job_id=job_id, filename=file.filename)
    
    return job_response

@app.get("/api/v1/status/{job_id}", response_model=ExcelJobResponse)
async def get_job_status(job_id: str):
    """작업 상태 조회"""
    
    if job_id not in excel_jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return excel_jobs[job_id]

@app.get("/api/v1/history")
async def get_job_history(limit: int = 10):
    """작업 히스토리 조회"""
    
    jobs = list(excel_jobs.values())
    jobs.sort(key=lambda x: x.created_at, reverse=True)
    
    return {
        "jobs": jobs[:limit],
        "total": len(jobs)
    }

async def _process_excel_merge(job_id: str, files: List[UploadFile]):
    """엑셀 파일 병합 처리 (pk_system 함수 활용)"""
    
    try:
        excel_jobs[job_id].status = "processing"
        
        logger.info("Starting excel merge", job_id=job_id)
        
        # 파일 데이터 읽기
        dataframes = []
        for file in files:
            content = await file.read()
            df = pd.read_excel(BytesIO(content))
            dataframes.append({
                "filename": file.filename,
                "data": df,
                "rows": len(df),
                "columns": len(df.columns)
            })
        
        # pk_system 함수 활용
        ensure_printed(f"Processing {len(dataframes)} Excel files", print_color='green')
        
        # 병합 로직
        merged_df = pd.concat([df_info["data"] for df_info in dataframes], ignore_index=True)
        
        # 결과 저장 (실제로는 S3나 DB에 저장)
        result = {
            "merged_rows": len(merged_df),
            "merged_columns": len(merged_df.columns),
            "source_files": [df_info["filename"] for df_info in dataframes],
            "download_url": f"https://example.com/downloads/{job_id}.xlsx"
        }
        
        excel_jobs[job_id].status = "completed"
        excel_jobs[job_id].result = result
        
        logger.info("Excel merge completed", job_id=job_id, merged_rows=len(merged_df))
        
    except Exception as e:
        excel_jobs[job_id].status = "failed" 
        excel_jobs[job_id].error = str(e)
        
        logger.error("Excel merge failed", job_id=job_id, error=str(e))

async def _process_excel_analysis(job_id: str, file: UploadFile):
    """엑셀 파일 분석 처리 (pk_system 함수 활용)"""
    
    try:
        excel_jobs[job_id].status = "processing"
        
        logger.info("Starting excel analysis", job_id=job_id)
        
        # 파일 데이터 읽기
        content = await file.read()
        df = pd.read_excel(BytesIO(content))
        
        # pk_system 함수로 데이터 분석
        ensure_printed(f"Analyzing Excel file: {file.filename}", print_color='blue')
        
        # 기본 분석
        analysis_result = {
            "filename": file.filename,
            "total_rows": len(df),
            "total_columns": len(df.columns),
            "column_names": df.columns.tolist(),
            "data_types": df.dtypes.to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "summary_stats": df.describe().to_dict() if len(df.select_dtypes(include=['number']).columns) > 0 else {},
            "sample_data": df.head().to_dict('records')
        }
        
        excel_jobs[job_id].status = "completed"
        excel_jobs[job_id].result = analysis_result
        
        logger.info("Excel analysis completed", job_id=job_id, rows=len(df))
        
    except Exception as e:
        excel_jobs[job_id].status = "failed"
        excel_jobs[job_id].error = str(e)
        
        logger.error("Excel analysis failed", job_id=job_id, error=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.excel_automation_port,
        reload=settings.debug
    )