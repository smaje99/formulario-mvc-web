from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///users.db')

Session = sessionmaker(bind=engine)

Base = declarative_base()

@contextmanager
def session_reading():
    session = Session()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()


@contextmanager
def session_writing():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
