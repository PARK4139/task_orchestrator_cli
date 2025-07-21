@echo off
chcp 65001 >nul

@REM requirements.txt 기반 구조에서 pyproject.toml 기반 구조 마이그레이션 시  → uv pip init
@REM 새 프로젝트이거나 requirements.txt 기반 구조 → uv pip install -r requirements.txt
@REM 새 프로젝트이거나 pyproject.toml + uv.lock 기반 구조    → uv sync
=%USERPROFILE%\Downloads\pk_system
cd %D_PK_SYSTEM%
uv sync
