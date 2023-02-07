from aiogram.types import Message
from psycopg2 import errors
from sqlalchemy.exc import IntegrityError

from db.models import session, BotsData
from db.models.users import Users


class DBActions:
    def __init__(self):
        self.session = session

    def add_new_user(self, message: Message):
        user_info = {'username': str(message.from_user.username),
                     'tg_id': message.from_user.id,
                     'tg_firstname': str(message.from_user.first_name)}
        try:
            new_user = Users(user_info)
            self.session.add(new_user)
            self.session.commit()
            self.session.close()

        except (IntegrityError, errors.UniqueViolation):
            self.session.close()
            self.add_new_visited_section('start_again', message.from_user.id)

    def add_new_visited_section(self, new_section: str, tg_id: int):
        update_user = self.session.query(Users).filter_by(tg_id=tg_id).first()
        update_user.visited_sections = update_user.visited_sections + ';' + new_section
        self.session.commit()
        self.session.close()

    def get_contacts(self):
        contacts = self.session.query(BotsData.contacts).first()
        return contacts
