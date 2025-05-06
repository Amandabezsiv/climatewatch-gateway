# create_user.py
from getpass import getpass
from gateway import db, models, auth


def create_user():
    db.init_db()
    session = db.SessionLocal()

    username = input("Enter username: ").strip()
    password = getpass("Enter password: ").strip()

    if session.query(models.User).filter_by(username=username).first():
        print("User already exists.")
        return

    hashed = auth.hash_password(password)
    user = models.User(username=username, hashed_password=hashed)
    session.add(user)
    session.commit()
    print(f"User '{username}' created.")


if __name__ == "__main__":
    create_user()
