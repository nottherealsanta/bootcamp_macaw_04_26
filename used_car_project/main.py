import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# col_list = ['Mileage_km',
#  'Year',
#  'Fuel_Consumption_l',
#  'Gears',
#  'Power_hp',
#  'Engine_Size_cc',
#  'Cylinders',
#  'Seats',
#  'Doors',
#  'Previous_Owners']

# model = joblib.load("./data/random_forest_model.pkl")

# def main():
#     print("Hello from used-car-project!")
#     inf_df = pd.read_csv("./data/inference_data.csv").sample(1)

#     X = inf_df[col_list]

#     predictions = model.predict(X)
#     print(predictions)

# if __name__ == "__main__":
#     main()

app = FastAPI()

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

model = joblib.load("./data/random_forest_model.pkl")

@app.post("/predict")
def predict_price(features: CarFeatures):
    print(features)
    # Convert the features to a DataFrame
    X = pd.DataFrame([features.dict()])

    # Make predictions
    predictions = model.predict(X)
    return {"predicted_price": predictions[0]}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Used Car Price Prediction API"}