import logging
import time
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from .engine import engine, async_engine
from app.exceptions.custom_exceptions import DBConnectionError

# Obtain a logger instance from the configured logging setup
logger = logging.getLogger('app.db.session')  # 'app' logger is defined in your logging_config.py

# Synchronous Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Asynchronous Session
AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)


def handle_db_exception(e: Exception, retry_count: int):
    if isinstance(e, exc.DBAPIError):
        logger.warning(f"Database connection error: {e}. Retry attempt: {retry_count}", exc_info=True)
    else:
        logger.error(f"Database error: {e}", exc_info=True)


# Dependency to get the DB session for sync operations
def get_db():
    retry_count = 0
    while retry_count < 3:
        db = SessionLocal()
        try:
            yield db
            break  # if successful, break out of the loop
        except Exception as e:  # Catch database connection errors and other exceptions
            retry_count += 1
            handle_db_exception(e, retry_count)
            time.sleep(2)  # sleep for 2 seconds before retrying
            if retry_count == 3:
                raise DBConnectionError(detail=str(e))
        finally:
            db.close()


# Dependency to get the DB session for async operations
async def get_db_async():
    async with AsyncSessionLocal() as session:
        yield session
