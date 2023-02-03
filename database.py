from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import boto3
from botocore.exceptions import ClientError
import json
from logger import logger

def get_secret():

    secret_name = "excluyeSecreto"
    region_name = "us-east-1"
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
    return get_secret_value_response['SecretString']


def database_connection_url():
    secret = json.loads(get_secret())
    return f"postgresql+psycopg2://{secret['username']}:{secret['password']}@{secret['host']}:{secret['port']}/{secret['dbname']}"




def get_db_proxy():
    import boto3
    proxy = boto3.resource('arn:aws:rds:us-east-1:365248273988:db-proxy:prx-07ceb259f4a205fc7')['excluyeproxy']
    return proxy


# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:R0mz5xapTozEUt8bhVut@35.174.92.84/excluye"
SQLALCHEMY_DATABASE_URL = database_connection_url()
#SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://excluyeproxy.proxy-cadtbsyxljrc.us-east-1.rds.amazonaws.com"
logger.info("Felipe conectandose a base de datos: "+SQLALCHEMY_DATABASE_URL[0:32]+"..."+SQLALCHEMY_DATABASE_URL[-20:])


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()