from sqlalchemy import Table, Column, Integer, String
from app.sql_app.database import meta

signo = Table('signos', meta,
              Column('id', Integer, primary_key=True),
              Column('nome', String(45)))
