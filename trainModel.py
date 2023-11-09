import json
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import sys


def train_model():
    jsondata=json.loads(sys.argv[1])
    
    df = pd.DataFrame(jsondata)

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    df['hour'] = df['timestamp'].dt.hour
    df['minute'] = df['timestamp'].dt.minute
    df['second'] = df['timestamp'].dt.second

    target = 'temperature'

    X = df[['hour', 'minute', 'second']]
    y = df[target]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, 'trained_model.joblib')

    response_data = { "model":"trained"}
    try:
        print(json.dumps(response_data))
    except Exception as e:
        print(f"An error occurred: {e}")
train_model()    

