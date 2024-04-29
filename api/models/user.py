from sqlalchemy import Column, Integer, String
from api.extensions import db


class User(db.Model):  # type: ignore
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    login = Column(String, unique=True)
    password_hash = Column(String)
