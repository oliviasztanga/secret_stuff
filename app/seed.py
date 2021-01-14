from models import User, Post
import datetime

def seed(db):
    users = [

    ]

    posts = [

    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()