from sqlalchemy import create_engine, MetaData

user_db = 'root'
pass_db = 'MasterOv'
host = '127.0.0.1'

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{user_db}:{pass_db}@{host}:3306/prova_cbm'
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_dump.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

meta = MetaData()
connection = engine.connect()
