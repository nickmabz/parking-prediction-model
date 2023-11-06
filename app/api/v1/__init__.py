from fastapi import APIRouter

from app.api.v1.prediction.routes import router as pred_router

router = APIRouter()


router.include_router(pred_router, prefix="/pred", tags=["Prediction Module"])
