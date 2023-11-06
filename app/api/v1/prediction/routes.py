from typing import Any
import pandas as pd
from fastapi import APIRouter, HTTPException
from app.api.v1.prediction.schemas import PredictionInput, PredictionFeedback, PredictionResponse
from app.api.v1.prediction.models import PredictionModel
import joblib
import logging
from scipy import sparse


router = APIRouter()

# Configure your logger
logger = logging.getLogger(__name__)

# Load the trained model (make sure the path is correct)
model = PredictionModel.load_model("./analysis/parking_prediction_model.joblib")


def preprocess_input_data(input_data: PredictionInput, preprocessor, feature_names) -> pd.DataFrame:
    # Convert the input data to a DataFrame
    input_df = pd.DataFrame([input_data.dict()])

    # Preprocess the input data using the preprocessor used during training
    processed_input_df = preprocessor.transform(input_df)

    # If the output is a sparse matrix, convert it to a dense format
    if sparse.issparse(processed_input_df):
        processed_input_df = processed_input_df.todense()

    # Create a DataFrame with the correct feature names
    processed_input_df = pd.DataFrame(processed_input_df, columns=feature_names)

    return processed_input_df


@router.post("/predict", response_model=PredictionResponse, status_code=200)
async def make_prediction(input_data: PredictionInput):
    try:
        # Load the preprocessor and feature names
        preprocessor = joblib.load("./analysis/preprocessor.joblib")
        feature_names = joblib.load("./analysis/feature_names.joblib")

        # Preprocess the input data
        data_for_prediction = preprocess_input_data(input_data, preprocessor, feature_names)

        # Make prediction using the model
        prediction = model.predict(data_for_prediction)
        # Round the prediction to the nearest integer
        prediction_result = int(round(prediction[0])) if prediction.size == 1 else [int(round(pred)) for pred in
                                                                                    prediction]

        # Calculate percentage occupancy with precision
        capacity = input_data.capacity
        percentage_occupancy = (prediction_result / capacity) * 100
        # Calculate remaining spaces and round to the nearest integer
        remaining_spaces = int(capacity - prediction_result)

        # Construct the response object
        response_data = {
            "predicted_occupancy": prediction_result,
            "percentage_occupancy": round(percentage_occupancy, 2),
            "remaining_spaces": remaining_spaces
        }

        return PredictionResponse(
            success=True,
            code=200,
            message="Prediction made successfully.",
            data=response_data
        )
    except Exception as e:
        logger.error(f"Prediction error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An error occurred during prediction.")


def store_feedback(feedback_data: PredictionFeedback):
    # Implement actual storage logic here
    logger.info(f"Feedback received: {feedback_data}")


@router.post("/feedback", status_code=200)
async def receive_feedback(feedback_data: PredictionFeedback):
    try:
        store_feedback(feedback_data)
        return {"detail": "Feedback received successfully."}
    except Exception as e:
        logger.error(f"Feedback storage error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An error occurred while storing feedback.")
