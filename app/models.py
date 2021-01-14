from app import db


class User(db.Model):
    __tablename__ = "users"

    def serialize(self):
        return {}


class Post(db.Model):
    __tablename__ = "posts"


    def serialize(self):
        return {}