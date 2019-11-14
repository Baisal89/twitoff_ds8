from decouple import config
from flask import Flask, render_template, request
from .models import DB, User

#now we make a app factory

def create_app():
    app = Flask(__name__)

    #add out config
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #now have the database know about the app

    DB.init_app(app)


    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html',  tittle='Home')

    #adding in a new route to add users or get users
    @app.route('/user', methods=['POST'])# uses form
    @app.route('/user/<name>', methods=['GET'])#needs parameter
    def user(name=None, message=''):
        name = name or request.values['user_name']
        try:
            if request.method='POST':
                add_or_update_user(name)
                message="User {} successfully added!".format(name)
            tweets = User.query.filter(User.name == name).one().tweets
        except Exception as e:
            message = "Error adding {}: {}".format(name,e)
            tweets = []
        return render_template('user.html', title=name, tweets=tweets,
        message=message)

    @app.route('/reset')
    def reset():
        DB.drop.all()
        DB.create_app()
        return render_template('base.html',  tittle='Reset', users=[])

    return app
