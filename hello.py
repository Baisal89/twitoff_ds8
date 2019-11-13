""" Minimal flask app"""

from flask import Flask

#Make the applocation
app = Flask(__name__)


#make the route

@app.route("/")

#now we define a fucntion

def hello():
    return "hello beautiful world!"
