""" Minimal flask app"""

from flask import Flask, render_template

#Make the applocation
app = Flask(__name__)


#make the route

@app.route("/")

#now we define a fucntion

def hello():
    return render_template('home.html')


    #creating another route

@app.route("/about")

def preds():
    return render_template('about.html')
