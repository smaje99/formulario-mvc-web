from typing import List

from .schemas import User


data: List[User] = []

id: int = 0


def get_users() -> List[User]:
    return list(map(dict, data))


def get_user(alias: str) -> User:
    user = list(filter(
        lambda user: user.alias == alias, data))
    return user[0]


def add_user(user: User) -> User:
    global id
    id += 1
    user.id = id
    data.append(user)
    return get_user(user.alias)


def update_user(user: User) -> User:
    for i, user_data in enumerate(data):
        if user_data.alias == user.alias:
            data[i] = user
            return data[i]
