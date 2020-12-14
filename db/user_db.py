from typing import  Dict
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from db.db_conection import Base, engine


class UserInDB(BaseModel):
    __tablename__ = "users"
    username = Column(String, primary_key=True, unique=True)
    password = Column(String)
    balance = Column(Integer)

Base.metadata.create_all(bind=engine)

database_users = Dict[str, UserInDB]

database_users = {
    "camilo24": UserInDB(**{"username":"camilo24",
                            "password":"root",
                            "balance":12000}),

    "andres18": UserInDB(**{"username":"andres18",
                            "password":"hola",
                            "balance":34000}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db
