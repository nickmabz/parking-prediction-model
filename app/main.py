from fastapi import FastAPI
from app.exceptions.handlers import setup_exception_handlers
from app.core.logging_config import setup_logging

# Routes
from app.health import router as health_router
from app.api.v1 import router as api_v1_router

# Set up global logging
setup_logging()

# Create FastAPI app
app = FastAPI(
    title="Parking Predict",
    description="A model for predicting parking availability",
    version="1.0.0",
)

setup_exception_handlers(app)

# Register routers
app.include_router(api_v1_router, prefix="/v1")
app.include_router(health_router, prefix="/app", tags=["API Health"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
