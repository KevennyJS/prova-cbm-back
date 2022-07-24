from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy import Integer, String, DateTime
from sql_app import meta

perfis = Table('perfis', meta,
               Column('id', Integer, primary_key=True),
               Column('tipos_sanguineo_id', Integer),
               # Column('signo_id', Integer),
               # Column('tipo_sanguineo_id', Integer, ForeignKey('tipos_sanguineos.id')),
               Column('signo_id', Integer, ForeignKey('signos.id')),
               Column('cpf', String),
               Column('nome', String),
               Column('data_nascimento', DateTime),
               Column('email', String),
               Column('telefone', String),
               Column('resumo', String))
