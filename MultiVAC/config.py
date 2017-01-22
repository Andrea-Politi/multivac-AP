import os
from redis import Redis
from pymongo import MongoClient
import logging
import sys

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class BaseConfiguration(object):
    APP_ENV = os.environ.get("APP_ENV")
    WTF_CSRF_ENABLED = False
    DEBUG = os.environ.get("DEBUG_MODE") == "True"
    MONGODB_SETTINGS = {
        'db': os.environ.get("MONGO_DB_NAME"),
        'host': os.environ.get("MONGO_URL")
    }

    SECRET_KEY = os.environ.get("SECRET_KEY")

    FORCE_ENGINE = os.environ.get("FORCE_ENGINE", None)


class TestConfiguration(BaseConfiguration):
    TESTING = True
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': 'multivac_test',
    }


def get_env_var(varname):
    import os
    from dotenv import load_dotenv

    load_dotenv('.env')

    return os.environ.get(varname)


def get_redis_connection():
    # Redis connection
    r = get_env_var("REDIS_URL")
    redis_host, redis_port = r.split('/')[2].split(':')
    #redis_connection = Redis(host=redis_host, port=redis_port)
    redis_connection = Redis(host='localhost', port='6379')

    return redis_connection
    #print(redis_connection)


def get_multivac_db():
    # Connect to the mongodb db
    username = os.environ.get("multivac")
    password = os.environ.get("multivac")
    server = os.environ.get("127.0.0.1")

    # To account for local, protection-less dbs
    if password == "":
        mongourl = "mongodb://%s" % server
    else:
        mongourl = "mongodb://%s:%s@%s/%s" % (username, password, server, "multivac")

    log.debug("Connecting to the %s mongo database." % mongourl)
    client = MongoClient('localhost', 27017)
    db = client.get_database("multivac")

    return db
