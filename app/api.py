from flask import request, render_template, redirect
from app import app, db
from models import User, Post

@app.route('/', methods=['GET'])
def get_index():
    all_posts = Post.query.all()
    serialized_all_posts = [item.serialize() for item in all_posts]
    return render_template('index.html', all_posts=serialized_all_posts)

@app.route('/user/<string:username>', methods=['GET'])
def get_posts_by_user(username):
    user = User.query.filter_by(username=username).first()
    serialized_user = user.serialize()
    return render_template('user.html', user=serialized_user)

@app.route('/post/new', methods=['POST'])
def submit_new_post():
    username=request.form["username"]
    content=request.form["content"]
    user = User.query.filter_by(username).first()
    if user == None:
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
    post = Post(content=content, user_id=user.id)
    db.session.add(post)
    db.session.commit()
    return redirect('/')
