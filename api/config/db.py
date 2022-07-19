from sqlalchemy import create_engine, MetaData
import pymysql

engine = create_engine('mysql+pymysql://root:MasterOv@localhost:3306/prova_cbm', echo=True)

meta = MetaData()

connection = engine.connect()
