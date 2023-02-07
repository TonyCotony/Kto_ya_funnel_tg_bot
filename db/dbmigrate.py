from sqlalchemy import MetaData, create_engine, Table, Column, String, Integer, BigInteger, Boolean, ForeignKey, Date, \
    Time, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

from db.models import engine, Base
from settings import settings


def create_db():
    Base.metadata.create_all(engine)
    #
    metadata = MetaData()

    users = Table('users', metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('username', String(50)),
                  Column('tg_id', Integer, nullable=False),
                  Column('tg_firstname', String(50)),
                  Column('enter_date', DateTime, nullable=False),
                  Column('visited_sections', String),
                  Column('serial_not_purchased', DateTime),
                  Column('serial_purchase_date', DateTime),
                  Column('podcast_shadows_n_gifts_purchase_date', DateTime),
                  Column('podcasts_siddhi', DateTime)
                  )

    bots_data = Table('bots_data', metadata,
                      Column('id', Integer, primary_key=True),
                      Column("contacts", String),
                      Column("music_links", String),
                      Column("feedback", String),
                      Column("closed_group_link", String)
                      )

    metadata.create_all(engine)
    Base.metadata.create_all(engine)

    return print('schemas imported')


create_db()
