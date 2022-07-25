from sqlalchemy import create_engine, MetaData

user_db = 'root' #user do seu db
pass_db = '**sua senha**' #senha do seu db
host = 'localhost' #seu host

# Bases de migração de banco
# ==================================================
SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{user_db}:{pass_db}@{host}:3306/prova_cbm'
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_dump.db"
# ==================================================

engine = create_engine(SQLALCHEMY_DATABASE_URL)

meta = MetaData()
connection = engine.connect()
