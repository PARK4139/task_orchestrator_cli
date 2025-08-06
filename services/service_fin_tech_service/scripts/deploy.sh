#!/bin/bash

# Finance Investment Assistant Deployment Script

set -e

echo "🚀 Starting deployment of Finance Investment Assistant..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p logs
mkdir -p ssl

# Set environment variables
export DATABASE_URL="postgresql://finance_user:finance_password@localhost:5432/finance_db"
export REDIS_URL="redis://localhost:6379"

# Build and start services
echo "🔨 Building and starting services..."
cd infra
docker-compose up -d --build

# Wait for services to be ready
echo "⏳ Waiting for services to be ready..."
sleep 30

# Check service health
echo "🏥 Checking service health..."
services=("gateway" "recommendation-engine" "finance-api-client" "news-crawler")

for service in "${services[@]}"; do
    echo "Checking $service..."
    if curl -f http://localhost:8000/health > /dev/null 2>&1; then
        echo "✅ $service is healthy"
    else
        echo "❌ $service is not responding"
    fi
done

echo "🎉 Deployment completed successfully!"
echo ""
echo "📊 Service URLs:"
echo "  - API Gateway: http://localhost:8000"
echo "  - Recommendation Engine: http://localhost:8001"
echo "  - Finance API Client: http://localhost:8002"
echo "  - News Crawler: http://localhost:8003"
echo ""
echo "📚 API Documentation:"
echo "  - Swagger UI: http://localhost:8000/docs"
echo ""
echo "🛠️  Useful commands:"
echo "  - View logs: docker-compose logs -f"
echo "  - Stop services: docker-compose down"
echo "  - Restart services: docker-compose restart" 