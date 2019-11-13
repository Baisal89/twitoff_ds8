""" Entry point for out twitoff flask app"""

from .app import create_app

#APP is global variable
APP = create_app()

#run this in terminal with FLAKS_APP=TWITOFF:APP flask run 
