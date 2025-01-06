import os
from typing import Optional

import numpy as np
from helpers import load_pickle, save_pickle
from loguru import logger
from modeling import evaluate_model, predict, train_model
from prefect import flow
from preprocessing import process_data
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression

@flow(name="Train model")
def train_model_workflow(
    train_filepath: str,
    test_filepath: str,
    artifacts_filepath: Optional[str] = None,
    api_url: str = "http://localhost:8000/api/log"
) -> dict:
    """Train a model, log progress to FastAPI, and save it to a file."""
    logger.info("Processing training data...")
    
    # Log progress to FastAPI
    requests.post(api_url, json={"message": "Started processing training data"})
    
    X_train, y_train, dv = process_data(filepath=train_filepath, with_target=True)
    
    logger.info("Processing test data...")
    requests.post(api_url, json={"message": "Started processing test data"})
    
    X_test, y_test, _ = process_data(filepath=test_filepath, with_target=True, dv=dv)
    
    logger.info("Training model...")
    requests.post(api_url, json={"message": "Started training model"})
    
    model = train_model(X_train, y_train)
    
    logger.info("Making predictions and evaluating...")
    requests.post(api_url, json={"message": "Started predictions"})
    
    y_pred = predict(X_test, model)
    rmse = evaluate_model(y_test, y_pred)

    if artifacts_filepath is not None:
        logger.info(f"Saving artifacts to {artifacts_filepath}...")
        save_pickle(os.path.join(artifacts_filepath, "dv.pkl"), dv)
        save_pickle(os.path.join(artifacts_filepath, "model.pkl"), model)

    # Log model completion
    requests.post(api_url, json={"message": "Model training completed"})

    return {"model": model, "dv": dv, "rmse": rmse}
import requests
import numpy as np
from prefect import flow
from helpers import load_pickle
from modeling import predict
from preprocessing import process_data

@flow(name="Batch predict")
def batch_predict_workflow(
    input_filepath: str,
    model: Optional[LinearRegression] = None,
    dv: Optional[DictVectorizer] = None,
    artifacts_filepath: Optional[str] = None,
    api_url: str = "http://localhost:8000/api/predict"
) -> np.ndarray:
    """Make predictions on new data and send results to FastAPI."""
    if dv is None:
        dv = load_pickle(os.path.join(artifacts_filepath, "dv.pkl"))
    if model is None:
        model = load_pickle(os.path.join(artifacts_filepath, "model.pkl"))
    
    # Log starting prediction
    requests.post(api_url, json={"message": "Started batch predictions"})
    
    X, _, _ = process_data(filepath=input_filepath, with_target=False, dv=dv)
    y_pred = predict(X, model)

    # Send predictions to FastAPI
    requests.post(api_url, json={"predictions": y_pred.tolist()})

    # Log completion of batch prediction
    requests.post(api_url, json={"message": "Batch prediction completed"})
    
    return y_pred
from fastapi import FastAPI
from pydantic import BaseModel
import logging

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define request model for logging
class LogMessage(BaseModel):
    message: str

# Define request model for predictions
class Predictions(BaseModel):
    predictions: list

@app.post("/api/log")
async def log_message(log: LogMessage):
    logger.info(f"Log from Prefect: {log.message}")
    return {"status": "Log received"}

@app.post("/api/predict")
async def receive_predictions(predictions: Predictions):
    logger.info(f"Received predictions: {predictions.predictions[:5]}...")  # Show only first 5 predictions
    return {"status": "Predictions received"}
 # 确保这里会触发任务和工作流的执行
