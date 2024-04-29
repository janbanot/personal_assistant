from api.run import app
from ..api import db  # type: ignore
from api.models.user import User
from werkzeug.security import generate_password_hash


def create_admin_user(email: str, login: str, password: str):
    hashed_password = generate_password_hash(password)
    new_user = User(email=email, login=login, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():  # Create an application context
        email = input("Enter email: ")
        login = input("Enter login: ")
        password = input("Enter password: ")
        create_admin_user(email, login, password)
        print("User created")
