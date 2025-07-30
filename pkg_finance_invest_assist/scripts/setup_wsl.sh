#!/bin/bash

# WSL 환경 설정 스크립트

echo "🐧 WSL 환경 설정을 시작합니다..."

# 시스템 업데이트
echo "📦 시스템 패키지 업데이트 중..."
sudo apt update && sudo apt upgrade -y

# Python 3.11 설치
echo "🐍 Python 3.11 설치 중..."
sudo apt install -y python3.11 python3.11-venv python3.11-dev python3-pip

# uv 설치 (Python 패키지 관리자)
echo "📦 uv 패키지 관리자 설치 중..."
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.cargo/env

# Docker 설치
echo "🐳 Docker 설치 중..."
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Docker 권한 설정
sudo usermod -aG docker $USER

# Git 설치 (이미 설치되어 있을 수 있음)
echo "📚 Git 설치 중..."
sudo apt install -y git

# 프로젝트 디렉토리 생성
echo "📁 프로젝트 디렉토리 설정 중..."
mkdir -p ~/projects
cd ~/projects

echo "✅ WSL 환경 설정이 완료되었습니다!"
echo ""
echo "🔄 다음 단계:"
echo "1. WSL을 재시작하거나 새 터미널을 열어주세요"
echo "2. cd ~/projects/pkg_finance_invest_assist"
echo "3. ./scripts/run_api.sh" 