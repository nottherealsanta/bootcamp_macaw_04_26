import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import logging
import datetime

app = FastAPI()

# levels of logging: DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()])

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

# model = joblib.load("./data/random_fores_model.pkl")
try: 
    model = joblib.load("./data/random_forest_model.pkl")
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")


@app.post("/predict")
def predict_price(features: CarFeatures):

    logging.info(f"Received features: {features}")
    try:
        # is Year > Current YEAR 
        year = features.Year
        current_year = datetime.datetime.now().year

        if year > current_year:
            logging.warning(f"Received year {year} is greater than the current year {current_year}")

        # Convert the features to a DataFrame
        X = pd.DataFrame([features.dict()])
        logging.debug(f"X.shape: {X.shape}")

        # Make predictions
        predictions = model.predict(X)
        return {"predicted_price": predictions[0]}
    except Exception as e:
        logging.error(f"Error making prediction: {e}")
        return {"error": "An error occurred while making the prediction"}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Used Car Price Prediction API"}