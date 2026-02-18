#!/bin/bash
# build.sh - Setup and build script for deployment

set -e  # Exit on error

echo "==================================="
echo "Building Constellation Predictor"
echo "==================================="

pip install uv

# Install system dependencies (for Linux)
if [ -f /etc/debian_version ]; then
    echo "Detected Debian/Ubuntu system"
    apt-get update -qq
    apt-get install -y --no-install-recommends libgl1 libglib2.0-0 2>/dev/null || true
fi

# Install Python dependencies
echo "Installing Python dependencies..."
uv sync

# Navigate to Django project
cd ConstellationPredictor

# Run database migrations
echo "Running database migrations..."
uv run manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
uv run manage.py collectstatic --noinput

echo "==================================="
echo "Build completed successfully!"
echo "==================================="
echo "Run ./start.sh to start the server"
