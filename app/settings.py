# -*- coding: utf-8 -*-
"""Application configuration.
Most configuration is set via environment variables.
For local development, use a .env file to set
environment variables.
"""

import os
import secrets
from loguru import logger
from starlette.config import Config

# get environment variables
config = Config(".env")
USE_ENV = config("USE_ENV", default="docker")
SECRET_KEY = secrets.token_urlsafe(64)

if USE_ENV.lower() == "dotenv":
    logger.info(f"USE_ENV set to {USE_ENV}. Using .env file for external configuration")
    # Application information
    APP_VERSION = config("APP_VERSION", default="1.0.0")
    RELEASE_ENV = config("RELEASE_ENV", default="prd")
    SQLALCHEMY_DATABASE_URI = config(
        "SQLALCHEMY_DATABASE_URI", default="sqlite:///sqlite_db/api.db"
    )
    # Loguru settings
    LOGURU_RETENTION = config("LOGURU_RETENTION", default="10 days")
    LOGURU_ROTATION = config("LOGURU_ROTATION", default="10 MB")
    LOGURU_LOGGING_LEVEL = config("LOGURU_LOGGING_LEVEL", default="WARNING")
    

else:
    logger.info(
        f"USE_ENV set to {USE_ENV}. Using os environmental settings for\
             external configuration"
    )
    # Application information
    APP_VERSION = os.environ["APP_VERSION"]
    # Application Configurations
    RELEASE_ENV = os.environ["RELEASE_ENV"]
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    # Loguru settings
    LOGURU_RETENTION = os.environ["LOGURU_RETENTION"]
    LOGURU_ROTATION = os.environ["LOGURU_ROTATION"]
    LOGURU_LOGGING_LEVEL = os.environ["LOGURU_LOGGING_LEVEL"]
