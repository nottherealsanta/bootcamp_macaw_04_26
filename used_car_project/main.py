import joblib
import pandas as pd

col_list = ['User ID', 'EstimatedSalary', 'Purchased']

model = joblib.load("../data/random_forest_model.pkl")

def main():
    print("Hello from FB Ads!")
    inf_df = pd.read_csv("../data/inference_data.csv").sample(1)

    X = inf_df[col_list]

    predictions = model.predict(X)
    print(predictions)

if __name__ == "__main__":
    main()
