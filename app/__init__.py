from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
# reads config settings from config.py
app.config.from_object('config')
# initialize the db, settings are also in config.py
db = SQLAlchemy(app)

from app import views, models
# views are handlers that respond to requests from web browsers or other clients
