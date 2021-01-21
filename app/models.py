from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))

    posts = db.relationship("Post", back_populates='user')

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "posts": [item.serialize() for item in self.posts],
        }


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(280))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="posts")

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "user_id": self.user_id,
            "user": self.user.username,
        }