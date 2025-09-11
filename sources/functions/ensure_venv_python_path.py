#!/usr/bin/env python3
"""
OS별 virtual environment Python 경로 관리
"""
import os
import platform
import sys
from pathlib import Path


def get_venv_python_path(task_orchestrator_cli_path: Path = None) -> str:
    """
    OS별 virtual environment Python 경로 반환
    
    Args:
        task_orchestrator_cli_path: task_orchestrator_cli 프로젝트 루트 경로 (None이면 자동 감지)
    
    Returns:
        str: virtual environment Python 실행 파일 경로
    """
    if task_orchestrator_cli_path is None:
        # 현재 파일에서 task_orchestrator_cli 루트 경로 자동 감지
        current_file = Path(__file__)
        task_orchestrator_cli_path = current_file.parent.parent.parent
    
    if platform.system().lower() == "windows":
        venv_python = task_orchestrator_cli_path / ".venv_windows" / "Scripts" / "python.exe"
    else:
        venv_python = task_orchestrator_cli_path / ".venv_linux" / "bin" / "python3"
    
    if venv_python.exists():
        return str(venv_python)
    else:
        # virtual environment 이 없으면 시스템 Python 사용
        return sys.executable


def get_venv_python_path_from_files() -> str:
    """
    files.py의 경로 상수를 사용하여 virtual environment Python 경로 반환
    
    Returns:
        str: virtual environment Python 실행 파일 경로
    """
    try:
        from sources.objects.task_orchestrator_cli_files import F_VENV_PYTHON_EXE, F_VENV_PYTHON_EXE
        
        if platform.system().lower() == "windows":
            if F_VENV_PYTHON_EXE.exists():
                return str(F_VENV_PYTHON_EXE)
        else:
            if F_VENV_PYTHON_EXE.exists():
                return str(F_VENV_PYTHON_EXE)
        
        # files.py 경로가 없으면 기본 방식 사용
        return get_venv_python_path()
        
    except ImportError:
        # files.py import 실패 시 기본 방식 사용
        return get_venv_python_path()


def ensure_venv_python_executed(task_orchestrator_cli_path: Path = None) -> None:
    """
    virtual environment Python으로 재실행 (필요한 경우)
    
    Args:
        task_orchestrator_cli_path: task_orchestrator_cli 프로젝트 루트 경로
    """
    venv_python = get_venv_python_path(task_orchestrator_cli_path)
    
    if venv_python != sys.executable and os.path.exists(venv_python):
        print(f"virtual environment Python으로 재실행: {venv_python}")
        try:
            os.execv(venv_python, [venv_python] + sys.argv)
        except OSError:
            # execv 실패 시 (Windows 등) 경고만 출력
            print(f"경고: virtual environment Python으로 재실행할 수 없습니다. 시스템 Python을 사용합니다.")


if __name__ == "__main__":
    print(f"현재 Python: {sys.executable}")
    print(f"Windows virtual environment Python: {get_venv_python_path()}")
    print(f"files.py 경로 사용: {get_venv_python_path_from_files()}")
