# app/schemas.py
from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    systemCodeNumber: str = Field(..., example="BHMBCCMKT01")
    hour: int = Field(..., ge=0, le=23, example=15)
    weekday: int = Field(..., ge=0, le=6, example=3)
    capacity: int = Field(..., ge=0, example=500)


class PredictionFeedback(BaseModel):
    systemCodeNumber: str = Field(..., example="BHMBCCMKT01")
    hour: int = Field(..., ge=0, le=23, example=15)
    weekday: int = Field(..., ge=0, le=6, example=3)
    capacity: int = Field(..., ge=0, example=500)
    occupancy: int = Field(..., ge=0, example=350)
    prediction: int = Field(..., ge=0, example=325)
    feedback: str = Field(..., example="The prediction was too low.")


class PredictionResponse(BaseModel):
    success: bool
    code: int
    message: str
    data: dict
