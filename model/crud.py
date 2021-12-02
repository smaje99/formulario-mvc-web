from sqlalchemy.orm import Session

from . import models, schemas


def get_user(self, session: Session, username: str) -> schemas.User:
    result = (session.query(models.User)
        .filter(models.User.username == username)
        .first())
    return schemas.User(**dict(result))


def add_user(self, session: Session, user: schemas.User):
    db_user = models.User(**dict(user))
    session.add(db_user)


def update_user(self, session: Session, user: schemas.User):
    (session.query(models.User)
        .filter(models.User.id == user.id)
        .update(dict(user)))
