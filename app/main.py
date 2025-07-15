from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ✅ add this
from pydantic import BaseModel
from model_utils import get_feature_names, predict_anomaly

app = FastAPI()

# ✅ Add CORS support to allow requests from browser frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to ["http://localhost:5500"] if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LogonInput(BaseModel):
    FailedLogons: int
    SuccessfulLogons: int
    SrcIpSuccessfulAccess: int
    ComputersSuccessfulAccess: int

@app.post("/predict_anomaly")
def predict(input_data: LogonInput):
    feature_names = get_feature_names()
    input_vector = [getattr(input_data, feat) for feat in feature_names]
    result = predict_anomaly(input_vector)
    return result
