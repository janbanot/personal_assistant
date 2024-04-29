from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .user import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("id", "email", "login", "password_hash")
