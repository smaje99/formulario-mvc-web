from fastapi import FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles

from model import crud, User


app = FastAPI()


@app.get('/users/')
def get_users():
    return crud.get_users()


@app.get('/users/{alias}', response_model=User)
def get_user(alias: str):
    try:
        user = crud.get_user(alias)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='El usuario no existe',
            headers={ 'WWW-Authenticate': 'Basic' }
        )
    return user


@app.post('/users/', response_model=User)
def create_user(user: User):
    return crud.add_user(user)


@app.put('/users/', response_model=User)
def update_user(user: User):
    return crud.update_user(user)


app.mount(
    '/',
    StaticFiles(directory='view', html=True),
    name='static'
)