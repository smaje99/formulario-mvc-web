from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from model import crud, User
from model.base import (
    Base,
    engine,
    session_reading,
    session_writing
)


Base.metadata.create_all(engine)

app = FastAPI()

app.mount(
    '/',
    StaticFiles(directory='view', html=True),
    name='static'
)


@app.get('/users/{username}', response_model=User)
def get_user(username: str, session: Session = Depends(session_reading)):
    try:
        user = crud.get_user(session, username)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='El usuario no existe',
            headers={ 'WWW-Authenticate': 'Basic' }
        )
    return user


@app.post('/users/', response_model=User)
def create_user(user: User, session: Session = Depends(session_writing)):
    crud.add_user(session, user)
    return user


@app.put('/users/', response_model=User)
def update_user(user: User, session: Session = Depends(session_writing)):
    crud.update_user(session, user)
    return user
