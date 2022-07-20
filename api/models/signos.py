from sqlalchemy import Table, Column, Integer, String
from config.db import meta

signos = Table('signos', meta,
               Column('id', Integer, primary_key=True),
               Column('nome', String(50)))
