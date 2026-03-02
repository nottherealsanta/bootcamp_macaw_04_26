import pandas as pd 


def cal_bmi(df: pd.DataFrame) -> pd.DataFrame:  
    df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
    return df

