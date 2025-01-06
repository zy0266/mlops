from typing import List

import numpy as np
import pandas as pd
from loguru import logger
from sklearn.base import BaseEstimator
from sklearn.feature_extraction import DictVectorizer
import sys
import os

# Add the path to the 'lib' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib')))

# Now you can import models
from models import InputData  # 

#from lib.models import InputData
from preprocessing import CATEGORICAL_COLS, encode_categorical_cols
import os


def run_inference(input_data: List[InputData], dv: DictVectorizer, model: BaseEstimator) -> np.ndarray:
    """Run inference on a list of input data.

    Args:
        payload (dict): the data point to run inference on.
        dv (DictVectorizer): the fitted DictVectorizer object.
        model (BaseEstimator): the fitted model object.

    Returns:
        np.ndarray: the predicted trip durations in minutes.

    Example payload:
        {'x': 0.2, 'y': 0.2, 'z': 0.2}
    """
    logger.info(f"Running inference on:\n{input_data}")
    df = pd.DataFrame([x.dict() for x in input_data])
    df = encode_categorical_cols(df)
    dicts = df[CATEGORICAL_COLS].to_dict(orient="records")
    X = dv.transform(dicts)
    y = model.predict(X)
    logger.info(f"price:\n{y}")
    return y
import os
print(f"Current working directory: {os.getcwd()}")
# Saving the preprocessor
