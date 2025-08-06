@echo off
REM Finance Investment Assistant Deployment Script for Windows

echo 🚀 Starting deployment of Finance Investment Assistant...

REM Check if Docker is installed
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker is not installed. Please install Docker first.
    exit /b 1
)

REM Check if Docker Compose is installed
docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker Compose is not installed. Please install Docker Compose first.
    exit /b 1
)

REM Create necessary directories
echo 📁 Creating necessary directories...
if not exist logs mkdir logs
if not exist ssl mkdir ssl

REM Set environment variables
set DATABASE_URL=postgresql://finance_user:finance_password@localhost:5432/finance_db
set REDIS_URL=redis://localhost:6379

REM Build and start services
echo 🔨 Building and starting services...
cd infra
docker-compose up -d --build

REM Wait for services to be ready
echo ⏳ Waiting for services to be ready...
timeout /t 30 /nobreak >nul

REM Check service health
echo 🏥 Checking service health...
curl -f http://localhost:8000/health >nul 2>&1
if errorlevel 1 (
    echo ❌ Services are not responding
) else (
    echo ✅ Services are healthy
)

echo 🎉 Deployment completed successfully!
echo.
echo 📊 Service URLs:
echo   - API Gateway: http://localhost:8000
echo   - Recommendation Engine: http://localhost:8001
echo   - Finance API Client: http://localhost:8002
echo   - News Crawler: http://localhost:8003
echo.
echo 📚 API Documentation:
echo   - Swagger UI: http://localhost:8000/docs
echo.
echo 🛠️  Useful commands:
echo   - View logs: docker-compose logs -f
echo   - Stop services: docker-compose down
echo   - Restart services: docker-compose restart

pause 