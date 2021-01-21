from models import User, Post
import datetime

def seed(db):
    users = [
        User(id=1, username="bilbo"),
        User(id=2, username="barbie"),
    ]

    posts = [
        Post(
            id=1,
            content="Hello, my name is Bilbo. I am looking for a friend to accompany to Mordor.",
            user_id=1,
        ),
        Post(
            id=2,
            content="Hello, I'm Barbie and I just found a really cool ring!!!",
            user_id=2,
        )
    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()