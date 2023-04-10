import cx_Oracle
import config

cx_Oracle.init_oracle_client(lib_dir=config.PATH_TO_ORACLE_CLIENT)

def connect():
    return cx_Oracle.connect(config.CONNECTION_STRING)
