import joblib
import pandas as pd

col_list = ['Mileage_km',
 'Year',
 'Fuel_Consumption_l',
 'Gears',
 'Power_hp',
 'Engine_Size_cc',
 'Cylinders',
 'Seats',
 'Doors',
 'Previous_Owners']

model = joblib.load("./data/random_forest_model.pkl")

def main():
    print("Hello from used-car-project!")
    inf_df = pd.read_csv("./data/inference_data.csv").sample(1)

    X = inf_df[col_list]

    predictions = model.predict(X)
    print(predictions)

if __name__ == "__main__":
    main()
