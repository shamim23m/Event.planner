# config.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS
import os

# Initialize app, database, and CORS
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/app.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'  # Change this for production

# Set up CORS to allow cross-origin requests
CORS(app)

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
