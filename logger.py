import logging

# Disable uvicorn access logger
#uvicorn_access = logging.getLogger("uvicorn.access")
#uvicorn_access.disabled = True

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.getLevelName(logging.DEBUG))

logger = logging.getLogger()
logger.setLevel(logging.INFO)
