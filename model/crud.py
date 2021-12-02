from typing import List

from .schemas import User


data: List[User] = []

id: int = 0


def get_users() -> List[User]:
    return data


def get_user(alias: str) -> User:
    user = list(filter(
        lambda user: user.alias == alias, data))

    if not user: raise Exception("No user found")

    return user[0]


def add_user(user: User) -> User:
    global id
    id += 1
    user.id = id
    data.append(user)
    return get_user(user.alias)


def update_user(user: User) -> User:
    for user_data in data:
        if user_data.id == user.id:
            user_data = user
            return user

    raise Exception("User not found")
