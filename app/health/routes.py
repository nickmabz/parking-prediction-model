import logging.config
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db_async
from app.exceptions.custom_exceptions import DBConnectionError

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/test-db", response_model=dict)
async def test_db(db: AsyncSession = Depends(get_db_async)):
    try:
        result = await db.execute(text("SELECT 1"))
        value = result.scalar()  # Use scalar() to fetch single value, it also fetches None if no result
        if value == 1:
            return {"success": True, "message": "Connected successfully to the database!"}
        else:
            raise DBConnectionError(detail="Failed to connect to the database.")

    except DBConnectionError as db_err:
        logger.error(f"Database connection error: {db_err.detail}")
        raise db_err  # This will be handled by the custom handler

    except Exception as e:
        logger.error(f"An unexpected error occurred while testing database connection: {e}")
        raise DBConnectionError(detail=f"Unexpected error: {e}")
