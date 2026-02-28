from pydantic import BaseModel
import logging
import pandas as pd
import joblib
import datetime
from fastapi import FastAPI
import sklearn

app = FastAPI()
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  handlers=[logging.FileHandler("app.log")])

class CarFeatures(BaseModel):
    Mileage_km: float
    Year: int
    Fuel_Consumption_l: float
    Gears: int
    Power_hp: int
    Engine_Size_cc: int
    Cylinders: int
    Seats: int
    Doors: int
    Previous_Owners: int

try:
    model = joblib.load(r'C:\Users\USER\Desktop\bootcamp_macaw_04_26\data\random_forest_model.pkl')
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

@app.post('/predict')
def predict(features: CarFeatures):
    try:
        logging.info(f'Received features {features}')
        X = pd.DataFrame([features.dict()])
        print(X)
        logging.debug(f"X.shape: {X.shape}")
        predictions = model.predict(X)
        print(predictions)

        return {"Prediction": predictions[0]}
    except Exception as e:
        logging.error(f"Error making predictions {e}")
        return {"Error": "An error occured while making the prediction"}

@app.get('/')
def landing():
    return {"message": "Welcome to the Car Price Prediction Application"}
    


