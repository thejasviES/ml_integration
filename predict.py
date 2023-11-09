import sys
import pandas as pd
import joblib


model = joblib.load('trained_model.joblib')

timestamp = sys.argv[1]

timestamp = pd.to_datetime(timestamp)
hour = timestamp.hour
minute = timestamp.minute
second = timestamp.second


input_data = pd.DataFrame({
    'hour': [hour],
    'minute': [minute],
    'second': [second]
})

prediction = model.predict(input_data)


print("Predicted Temperature:", prediction[0])

