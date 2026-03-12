1. Init the project with uv
```
uv init
```

2. Add your packages
```
uv add <package_name>
```

3. Run your main.py
```
uv run main.py
```

# Assignment

1. The best model possible
2. create a function in main.py, that accepts a dataframe of n rows, and returns a series of n rows with the prediction.

# docker 

`docker build -t used_car_price_estimation_model:v1 .`

`docker run -p 8000:8000 used_car_price_estimation_model:v1`

# testing it with curl
```curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Mileage_km": 50000,
    "Year": 2030,
    "Fuel_Consumption_l": 5.5,
    "Gears": 6,
    "Power_hp": 150,
    "Engine_Size_cc": 1968,
    "Cylinders": 4,
    "Seats": 5000000,
    "Doors": 5,
    "Previous_Owners": 1
  }'
  ```

