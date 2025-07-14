import joblib
from typing import List

# Load model and features once when the module is imported
model, feature_names = joblib.load("iso_model.pkl")

def get_feature_names() -> List[str]:
    """Return the list of feature names the model expects."""
    return feature_names

def predict_anomaly(input_vector: List[float]) -> dict:
    """
    Takes a list of feature values and returns:
    - anomaly: True if the data point is considered an anomaly
    - score: Isolation Forest anomaly score (higher = more normal)
    """
    score = model.decision_function([input_vector])[0]
    is_anomaly = model.predict([input_vector])[0] == -1
    return {
        "score": float(score),
        "anomaly": bool(is_anomaly)
    }
