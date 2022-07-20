from sqlalchemy import Table, Column, Integer, String
from config.db import meta

tipos_sanguineos = Table('tipos_sanguineos', meta,
                         Column('id', Integer, primary_key=True),
                         Column('nome', String(50)))
