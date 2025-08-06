#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# PK System – Finance Service build & test helper
# This script builds the finance micro-services with Docker Compose, runs them,
# performs a simple health-check, and finally shuts everything down.
# It is intended to be executed inside WSL/Linux.
# -----------------------------------------------------------------------------
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEPLOY_DIR="$PROJECT_ROOT/deployment"

echo "🔧 Fin-Service build script"
echo "📁 Project : $PROJECT_ROOT"

echo "⏳ Preparing environment…"
# 1) Ensure .env exists
if [[ -f "$PROJECT_ROOT/env.example" && ! -f "$PROJECT_ROOT/.env" ]]; then
  cp "$PROJECT_ROOT/env.example" "$PROJECT_ROOT/.env"
  echo "✅ .env created from env.example"
fi
# 2) Required directories
mkdir -p "$PROJECT_ROOT/logs" "$DEPLOY_DIR/ssl"

echo "🔨 docker compose build…"
docker compose -f "$DEPLOY_DIR/docker-compose.yml" build --pull

echo "🚀 docker compose up…"
docker compose -f "$DEPLOY_DIR/docker-compose.yml" up -d

# Wait for services
sleep 15

HEALTH_URL="http://localhost:8000/health"
echo "🔍 Health-check $HEALTH_URL"
if curl -fsSL "$HEALTH_URL" >/dev/null; then
  echo "🎉 Health-check OK"
  RESULT=0
else
  echo "💥 Health-check FAILED"
  RESULT=1
fi

echo "🧹 Shutting down containers…"
docker compose -f "$DEPLOY_DIR/docker-compose.yml" down

exit $RESULT
