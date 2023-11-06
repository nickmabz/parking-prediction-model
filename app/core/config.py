import logging
import os
from dotenv import load_dotenv, find_dotenv
from app.core.logging_config import setup_logging

# Set up global logging
setup_logging()

# Load environment variables from .env file
env_file = find_dotenv()
if env_file:
    load_dotenv(env_file)
else:
    logging.warning("No .env file found. Running with system environment variables.")

# Common configurations
SECRET_KEY = os.getenv("SECRET_KEY", "your-fallback-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "RS256")

# Database Values
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Database connection pool configurations
POOL_SIZE = int(os.getenv("DB_POOL_SIZE", 10))
MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", 10))
POOL_RECYCLE = int(os.getenv("DB_POOL_RECYCLE", 300))
POOL_TIMEOUT = int(os.getenv("DB_POOL_TIMEOUT", 30))


def construct_db_url(user, password, host, port, db_name, driver=''):
    return f"postgresql{driver}://{user}:{password}@{host}:{port}/{db_name}"


SQLALCHEMY_DATABASE_URL = construct_db_url(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
SQLALCHEMY_DATABASE_URL_ASYNC = construct_db_url(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME, '+asyncpg')
