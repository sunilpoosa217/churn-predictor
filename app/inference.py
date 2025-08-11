import os
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_PATH = os.environ.get("MODEL_PATH", "model/churn_pipeline.joblib")
model = joblib.load(MODEL_PATH)

FEATURES = ["Geography","NumOfProducts","HasCrCard","Tenure","Gender",
            "CreditScore","IsActiveMember","Balance","Age","EstimatedSalary"]

class Payload(BaseModel):
    Geography: str
    NumOfProducts: float
    HasCrCard: bool
    Tenure: float
    Gender: str
    CreditScore: float
    IsActiveMember: bool
    Balance: float
    Age: float
    EstimatedSalary: float

app = FastAPI(title="Churn Inference API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/infer")
def infer(payload: Payload):
    data = payload.dict()
    data["HasCrCard"] = 1.0 if data["HasCrCard"] else 0.0
    data["IsActiveMember"] = 1.0 if data["IsActiveMember"] else 0.0
    df = pd.DataFrame([data], columns=FEATURES)
    if hasattr(model, "predict_proba"):
        proba = float(model.predict_proba(df)[0, 1])
    else:
        proba = float(model.predict(df)[0])
    pred = int(proba >= 0.5)
    return {"prediction": pred, "probability": proba}
