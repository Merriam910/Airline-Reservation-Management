import config
import cx_Oracle
from sqlalchemy import create_engine

def create_engine_with_oracle_client():
    cx_Oracle.init_oracle_client(lib_dir=config.PATH_TO_ORACLE_CLIENT)
    engine = create_engine(f'oracle+cx_oracle://{config.USERNAME}:{config.PASSWORD}@{config.HOST}:{config.PORT}/{config.DATABASE}')
    return engine


engine = create_engine_with_oracle_client()
