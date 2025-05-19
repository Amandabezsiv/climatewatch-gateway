# create_user.py
from getpass import getpass
from gateway import db, models, auth
from models import User
from db import SessionLocal
from auth import hash_password


def create_user():
    db.init_db()
    session = SessionLocal()

    username = input("Enter username: ").strip()
    password = getpass("Enter password: ").strip()

    if session.query(models.User).filter_by(username=username).first():
        print("User already exists.")
        return

    hashed = hash_password(password)
    user = User(username=username, hashed_password=hashed)
    session.add(user)
    session.commit()
    print(f"User '{username}' created.")


if __name__ == "__main__":
    create_user()
