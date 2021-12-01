from fastapi import FastAPI

from model import Database, User


db = Database()

app = FastAPI()


@app.get('/')
def get_user(username: str):
    return db.get_user(username)


@app.post('/')
def create_user(user: User):
    db.add_user(user)


@app.put('/')
def update_user(user: User):
    db.update_user(user)
