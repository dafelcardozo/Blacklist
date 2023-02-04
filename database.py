from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import boto3
import json
from logger import logger
import os


def get_secret():
    secret_name = "excluyeSecreto"
    region_name = "us-east-1"
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
    return get_secret_value_response['SecretString']

def database_connection_url():
    secret = json.loads(get_secret())
    return f"postgresql+psycopg2://{secret['username']}:{secret['password']}@{secret['host']}:{secret['port']}/{secret['dbname']}"

BLACKLIST_DATABASE_URL = os.environ.get("BLACKLIST_DATABASE_URL", None)
SQLALCHEMY_DATABASE_URL = BLACKLIST_DATABASE_URL if BLACKLIST_DATABASE_URL != None else database_connection_url()

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()