from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from app.core.config import (SQLALCHEMY_DATABASE_URL, SQLALCHEMY_DATABASE_URL_ASYNC,
                             POOL_SIZE, MAX_OVERFLOW, POOL_TIMEOUT, POOL_RECYCLE)

# Synchronous Engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=POOL_SIZE,
    max_overflow=MAX_OVERFLOW,
    pool_timeout=POOL_TIMEOUT,
    pool_recycle=POOL_RECYCLE,
    echo=False
)

# Asynchronous Engine
async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL_ASYNC,
    pool_size=POOL_SIZE,
    max_overflow=MAX_OVERFLOW,
    pool_timeout=POOL_TIMEOUT,
    pool_recycle=POOL_RECYCLE,
    echo=False
)
