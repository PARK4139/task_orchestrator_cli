@echo off
chcp 65001 >nul

@REM requirements.txt 기반 구조에서 pyproject.toml 기반 구조 마이그레이션 시  → uv pip init
@REM 새 프로젝트이거나 requirements.txt 기반 구조 → uv pip install -r requirements.txt
@REM 새 프로젝트이거나 pyproject.toml + uv.lock 기반 구조    → uv sync --active
set D_TASK_ORCHESTRATOR_CLI=%USERPROFILE%\Downloads\task_orchestrator_cli
cd %D_TASK_ORCHESTRATOR_CLI%
@REM Windows용 .venv_windows virtual environment 으로 uv sync --active 실행
set UV_PROJECT_ENVIRONMENT=.venv_windows
uv sync --active
