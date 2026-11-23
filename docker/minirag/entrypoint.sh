#!/bin/bash
set -e

echo "Running database migrations..."
cd /app/models/db_schemes/minirag/
python -c "from alembic.config import main; main(['upgrade', 'head'])"
cd /app

echo "Starting application..."
exec "$@"
