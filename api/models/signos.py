from sqlalchemy import Table, Column, Integer, String
from config.db import meta

signo = Table('signos', meta,
              Column('id', Integer, primary_key=True),
              Column('nome', String))
