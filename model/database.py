from base import Base, engine, session_reading, session_writing
from user import User


class Database:
    def __init__(self):
        Base.metadata.create_all(engine)

    def get_user(self, username: str):
        with session_reading as session:
            result = (session.query(User)
                        .filter(User.username == username)
                        .first())
        return result

    def add_user(self, user: User):
        with session_writing() as session:
            session.add(user)

    def update_user(self, user: User):
        with session_writing() as session:
            (session.query(User)
                .filter(User.id == user.id)
                .update(dict(user)))
