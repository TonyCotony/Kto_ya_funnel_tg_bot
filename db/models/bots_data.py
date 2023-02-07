from sqlalchemy import Column, Integer, String

from db.models import Base


class BotsData(Base):
    __tablename__ = 'bots_data'
    id = Column(Integer, primary_key=True)
    contacts = Column(String)
    music_links = Column(String)
    feedback = Column(String)
    closed_group_link = Column(String)

    def __init__(self, contacts: str):
        self.contacts = contacts

    def __repr__(self):
        info: str = self.contacts
        return info
