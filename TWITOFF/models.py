"""These are my database models"""

from flask_sqlalchemy import SQLAlchemy

# import database. capital for gloval scope

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users that we analyze"""
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)


class Tweet(DB.Model):
    """The user's tweets form twitter"""
    id = DB.Column(DB.Integer, primary_key=True)
    text=DB.Column(DB.Unicode(200))
