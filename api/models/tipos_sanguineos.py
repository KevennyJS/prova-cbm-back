from sqlalchemy import Table, Column, Integer, String
from sql_app.database import meta

tipo_sanguineo = Table('tipos_sanguineos', meta,
                       Column('id', Integer, primary_key=True),
                       Column('nome', String(45)))
