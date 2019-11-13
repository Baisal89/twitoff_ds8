from flask import Flask
from .models import DB

#now we make a app factory

def create_app():
    app = Flask(__name__)

    #add out config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    #now have the database know abount the app

    DB.init_app(app)


    @app.route('/')
    def root():
        return "Wlcome to Twitoff"

    return app
