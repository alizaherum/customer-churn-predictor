from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model when API starts
model = joblib.load("model_xgb.pkl")

@app.get("/")
def home():
    return {"message": "Churn Predictor API is running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    probability = model.predict_proba(df)[0][1]
    return {
        "prediction": int(prediction[0]),
        "churn_probability": round(float(probability), 3)
    }
    
