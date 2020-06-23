# -*- coding: utf-8 -*-
"""
database simple functions. Pass query and where needed values and get result back
"""

import logging
from loguru import logger
from sqlalchemy.sql import text

from com_lib.db_setup import database


async def fetch_one_db(query):

    result = await database.fetch_one(query)
    logger.debug(str(result))
    return result


async def fetch_all_db(query):

    result = await database.fetch_all(query)
    logger.debug(str(result))
    return result


async def execute_one_db(query, values: dict):

    result = await database.execute(query, values)
    logger.debug(str(result))
    return result


async def execute_many_db(query, values: dict):

    result = await database.execute_many(query, values)
    logger.debug(str(result))
    return result
