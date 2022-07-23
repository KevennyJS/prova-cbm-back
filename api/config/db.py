from sqlalchemy import create_engine, MetaData

user_db = 'root'
pass_db = 'MasterOv'

engine = create_engine(f'mysql+pymysql://{user_db}:{pass_db}@localhost:3306/prova_cbm', echo=True)

meta = MetaData()

connection = engine.connect()
