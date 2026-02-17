#!/bin/bash
# start.sh - Start the Django development server

set -e  # Exit on error

echo "Starting Constellation Predictor server..."

# Navigate to Django project
cd ConstellationPredictor

# Start Django development server
uv run manage.py runserver 0.0.0.0:8000
