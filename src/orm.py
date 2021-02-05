from sqlalchemy import MetaData, Table, Column, String, Integer, Date, Time, \
    Float
from sqlalchemy.orm import mapper, relationship

from . import model

metadata = MetaData()

jobs = Table(
    'jobs', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('customer', Integer),
    Column('employees', String(255)),
    Column('date', Date),
    Column('start_time', Time),
    Column('end_time', Time),
    Column('hours_number', Float),
)


def start_mappers():
    jobs_mapper = mapper(model.Job, jobs)
