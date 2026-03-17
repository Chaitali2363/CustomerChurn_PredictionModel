
import os
import pandas as pd

#Path Configuration:

data_path = os.path.join('data','chrun.csv')
model_dir = os.path.join("models")
os.modeldirs(model_dir , exist_ok = True)
pickle_path = os.path.join(model_dir , "churn_model.pkl")

#Data Loading:

def data_ingestion():
    df = pd.read_csv(data_path)
    return df
