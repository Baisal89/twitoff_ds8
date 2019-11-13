from flask import Flask

#now we make a app factory

def create_app():
    app = Flask(__name__)


    @app.route('/')
    def root():
        return "Wlcome to Twitoff"

    return app 
