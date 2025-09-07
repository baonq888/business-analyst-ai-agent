#!/usr/bin/env bash
# Start the FastAPI app (development)
export PYTHONPATH="$(pwd)/src"
uvicorn src.api.main:app --reload --host 127.0.0.1 --port 8000
