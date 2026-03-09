import pytest 
import pandas as pd 

from sample_func import cal_bmi


@pytest.fixture
def sample_data():
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'height': [165, 180, 175],
        'weight': [68, 75, 70]
    }
    return pd.DataFrame(data)

def test_cal_bmi(sample_data):
    result = cal_bmi(sample_data)
    expected_bmi = [24.98, 23.15, 22.86]
    assert result['BMI'].tolist() == pytest.approx(expected_bmi, rel=1e-2)
    assert result['name'].tolist() == ['Alice', 'Bob', 'Charlie']

def test_cal_bmi_missing_column(sample_data):
    sample_data.drop(columns=['height'], inplace=True)
    with pytest.raises(KeyError):
        cal_bmi(sample_data)

@pytest.mark.parametrize("height, weight, expected_bmi", [
    (165, 68, 24.98),
    (180, 75, 23.15),
    (175, 70, 22.86)
])
def test_cal_bmi_parametrize(height, weight, expected_bmi):
    df = pd.DataFrame({'height': [height], 'weight': [weight]})
    result = cal_bmi(df)
    assert result['BMI'].iloc[0] == pytest.approx(expected_bmi, rel=1e-2)