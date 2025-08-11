# Churn Predictor API

FastAPI app serving a trained churn prediction model.

## Deploy to Render

1. Push this repo to GitHub.
2. On Render.com: New → Web Service → Connect GitHub → Select this repo.
3. Settings:
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.inference:app --host 0.0.0.0 --port 8000`
   - Instance: Free
   - Port: 8000

4. Click Create Web Service and wait for Live.

## API

### Health
GET `/health` → `{ "status": "ok" }`

### Predict
POST `/infer`
```json
{
    "Geography": "France",
    "NumOfProducts": 2,
    "HasCrCard": true,
    "Tenure": 5,
    "Gender": "Male",
    "CreditScore": 650,
    "IsActiveMember": true,
    "Balance": 50000.0,
    "Age": 35,
    "EstimatedSalary": 60000.0
}
```

Response:
```json
{"prediction": 0, "probability": 0.12}
```
