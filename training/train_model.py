import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv("logon_features.csv")
features = ["FailedLogons", "SuccessfulLogons", "SrcIpSuccessfulAccess", "ComputersSuccessfulAccess"]
X = df[features]

model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
model.fit(X)

joblib.dump((model, features), "../app/iso_model.pkl")
print("Model trained and saved to app/iso_model.pkl")
