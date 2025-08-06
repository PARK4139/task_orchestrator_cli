# PK System Enable Script (Windows PowerShell)
# Windows 환경에서 PK 시스템을 활성화하는 스크립트

param(
    [switch]$Verbose
)

# UTF-8 설정
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "🐍 PK System Enable Script (Windows PowerShell)" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan

# 현재 스크립트 위치
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$PROJECT_ROOT = $SCRIPT_DIR
$USER_HOME = $env:USERPROFILE

Write-Host "📁 Script directory: $SCRIPT_DIR" -ForegroundColor Yellow
Write-Host "📁 Project root: $PROJECT_ROOT" -ForegroundColor Yellow

# Python 찾기 함수
function Find-Python {
    Write-Host "🔍 Python 찾는 중..." -ForegroundColor Yellow
    
    # 1. 시스템 python 확인
    try {
        $pythonVersion = python --version 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ 시스템 Python 발견: python" -ForegroundColor Green
            return "python"
        }
    } catch {}
    
    # 2. python3 확인
    try {
        $pythonVersion = python3 --version 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ 시스템 Python 발견: python3" -ForegroundColor Green
            return "python3"
        }
    } catch {}
    
    # 3. 가상환경 python 확인
    $venvPython = Join-Path $PROJECT_ROOT ".venv\Scripts\python.exe"
    if (Test-Path $venvPython) {
        Write-Host "✅ 가상환경 Python 발견: $venvPython" -ForegroundColor Green
        return $venvPython
    }
    
    # 4. 전체 프로젝트에서 python 찾기
    $pythonFiles = Get-ChildItem -Path $PROJECT_ROOT -Recurse -Name "python*.exe" -ErrorAction SilentlyContinue
    if ($pythonFiles) {
        $firstPython = Join-Path $PROJECT_ROOT $pythonFiles[0]
        Write-Host "✅ Python 발견: $firstPython" -ForegroundColor Green
        return $firstPython
    }
    
    # Python을 찾을 수 없는 경우
    Write-Host "❌ Python을 찾을 수 없습니다." -ForegroundColor Red
    Write-Host "📥 Python 설치를 시도합니다..." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "다음 중 하나를 선택하세요:" -ForegroundColor Yellow
    Write-Host "1. python.org에서 수동 설치 (권장)" -ForegroundColor Yellow
    Write-Host "2. Microsoft Store에서 설치" -ForegroundColor Yellow
    Write-Host "3. 취소" -ForegroundColor Yellow
    Write-Host ""
    
    $choice = Read-Host "선택 (1-3)"
    
    switch ($choice) {
        "1" {
            Write-Host "🌐 python.org로 이동 중..." -ForegroundColor Yellow
            Write-Host "https://www.python.org/downloads/" -ForegroundColor Cyan
            Write-Host "설치 완료 후 이 스크립트를 다시 실행하세요." -ForegroundColor Yellow
            Start-Process "https://www.python.org/downloads/"
            exit 1
        }
        "2" {
            Write-Host "🛒 Microsoft Store에서 Python 설치 중..." -ForegroundColor Yellow
            Start-Process "ms-windows-store://pdp/?ProductId=9NRWMJP3717K"
            Write-Host "설치 완료 후 이 스크립트를 다시 실행하세요." -ForegroundColor Yellow
            exit 1
        }
        "3" {
            Write-Host "취소되었습니다." -ForegroundColor Yellow
            exit 1
        }
        default {
            Write-Host "잘못된 선택입니다." -ForegroundColor Red
            exit 1
        }
    }
}

# Python 찾기 실행
$PYTHON_CMD = Find-Python

# Python 스크립트 실행
Write-Host "🚀 Python 스크립트 실행 중: $PYTHON_CMD ensure_pk_system_enabled.py" -ForegroundColor Yellow
Set-Location $PROJECT_ROOT

if (Test-Path "ensure_pk_system_enabled.py") {
    & $PYTHON_CMD ensure_pk_system_enabled.py
    $EXIT_CODE = $LASTEXITCODE
    
    if ($EXIT_CODE -eq 0) {
        Write-Host "✅ 스크립트 실행 완료" -ForegroundColor Green
    } else {
        Write-Host "❌ 스크립트 실행 실패 (오류 코드: $EXIT_CODE)" -ForegroundColor Red
        exit $EXIT_CODE
    }
} else {
    Write-Host "❌ ensure_pk_system_enabled.py 파일을 찾을 수 없습니다." -ForegroundColor Red
    Write-Host "📁 현재 디렉토리: $(Get-Location)" -ForegroundColor Yellow
    Write-Host "📋 파일 목록:" -ForegroundColor Yellow
    Get-ChildItem *.py -ErrorAction SilentlyContinue | ForEach-Object { Write-Host "  $($_.Name)" }
    exit 1
}

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "✅ PK System Enable Script 완료" -ForegroundColor Green 