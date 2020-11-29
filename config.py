import os
from os import environ


#DEBUG = True

SECRET_KEY = "secret_key"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

REDIS_HOST = "0.0.0.0"
REDIS_PORT = 6379
BROKER_URL = environ.get('REDIS_URL', "redis://{host}:{port}/0".format(host=REDIS_HOST, port=str(REDIS_PORT)))
CELERY_RESULT_BACKEND = BROKER_URL
