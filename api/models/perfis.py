from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy import Integer, String, DateTime
from sql_app.database import meta

perfis = Table('perfis', meta,
               Column('id', Integer, primary_key=True),
               Column('tipos_sanguineo_id', Integer),
               # Column('tipos_sanguineo_id', Integer, ForeignKey('tipos_sanguineos.id')),
               Column('signo_id', Integer, ForeignKey('signos.id')),
               Column('cpf', String(11)),
               Column('nome', String(50)),
               Column('data_nascimento', DateTime),
               Column('email', String(45)),
               Column('telefone', String(45)),
               Column('resumo', String))
