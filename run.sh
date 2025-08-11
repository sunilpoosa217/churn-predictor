#!/usr/bin/env bash
set -euo pipefail
export MODEL_PATH="model/churn_pipeline.joblib"
uvicorn app.inference:app --host 0.0.0.0 --port 8000
