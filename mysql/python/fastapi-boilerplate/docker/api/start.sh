#!/bin/bash

echo "Waiting for mysql"

while ! nc -z db 3306; do
  sleep 0.1
done

echo "MySQL started"

exec "$@"

uvicorn src.server:app --host 0.0.0.0 --port 8000 --workers 1