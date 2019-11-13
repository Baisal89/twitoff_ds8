from flask import Flask, render_template, request
from .models import DB, User

#now we make a app factory

def create_app():
    app = Flask(__name__)

    #add out config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #now have the database know about the app

    DB.init_app(app)


    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html',  tittle='Home')

    return app
