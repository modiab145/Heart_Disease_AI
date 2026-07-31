import pandas as pd
import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

HISTORY_PATH = os.path.join(
    BASE_DIR,
    "history",
    "prediction_history.csv"
)


def save_prediction(age, sex, prediction, probability):

    new_record = pd.DataFrame({

        "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],

        "Age": [age],

        "Sex": [sex],

        "Prediction": [prediction],

        "Probability": [round(probability, 2)]

    })

    new_record.to_csv(

        HISTORY_PATH,

        mode="a",

        header=False,

        index=False

    )


def load_history():

    return pd.read_csv(HISTORY_PATH)