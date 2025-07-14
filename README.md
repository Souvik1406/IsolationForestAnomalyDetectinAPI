# Windows Logon Anomaly Detection API

An ML-powered FastAPI service that uses an Isolation Forest model to detect anomalies in Windows logon patterns.

## Usage
POST `/predict_anomaly` with:

```json
{
  "FailedLogons": 10,
  "SuccessfulLogons": 20,
  "SrcIpSuccessfulAccess": 3,
  "ComputersSuccessfulAccess": 2
}
