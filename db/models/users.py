import datetime

from sqlalchemy import Integer, String, Column, DateTime

from db.models import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    tg_id = Column(Integer, nullable=False, unique=True)
    tg_firstname = Column(String)
    enter_date = Column(DateTime, nullable=False)
    visited_sections = Column(String)
    serial_not_purchased = Column(DateTime)
    serial_purchased_date = Column(DateTime)
    podcast_shadows_n_gifts_purchase_date = Column(DateTime)
    podcasts_siddhi = Column(DateTime)

    def __init__(self, user_info: dict):
        self.username = user_info['username']
        self.tg_id = user_info['tg_id']
        self.tg_firstname = user_info['tg_firstname']
        self.enter_date = datetime.datetime.now()

    def __repr__(self):
        info: str = f'Пользователь - {str(self.username)}, {self.tg_id}\n' \
                    f'Дата входа в бота - {self.enter_date.date()}'
        return info
