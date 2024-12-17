# Load models
import joblib
import numpy as np

depression_model = joblib.load('models/depression_model.pkl')
anxiety_model = joblib.load('models/anxiety_model.pkl')
stress_model = joblib.load('models/stress_model.pkl')
happiness_model = joblib.load('models/happiness_model.pkl')

# Make predictions
def depression_pred(depression):
    depression = np.array(depression).reshape((1, -1))
    return depression_model.predict(depression)

def anxiety_pred(anxiety):
    anxiety = np.array(anxiety).reshape((1, -1))
    return anxiety_model.predict(anxiety)

def stress_pred(stress):
    stress = np.array(stress).reshape((1, -1))
    return stress_model.predict(stress)

def happy_pred(happy):
    happy = np.array(happy).reshape((1, -1))
    return int(happiness_model.predict(happy))