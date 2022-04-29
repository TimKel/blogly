from flask_sqlalchemy import SQLAlchemy
import datetime 

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

db = SQLAlchemy()




"""Models for Blogly."""
class User(db.Model):
    """User"""
    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name =  db.Column(db.String,
                            nullable=False)
    last_name = db.Column(db.String,
                            nullable=False)
    image_url = db.Column(db.String,
                            nullable=False,
                            default=DEFAULT_IMAGE_URL)

    posts = db.relationship('Post', backref='user')


class Post(db.Model):
    """Blog Posts"""
    __tablename__= "posts"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.String(50), 
                        nullable=False)
    content = db.Column(db.String,
                        nullable=False)
    created_at = db.Column(db.DateTime, 
                            nullable=False,
                            default=datetime.datetime.now)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'))


def connect_db(app):
    db.app = app
    db.init_app(app)