# database.py

from flask_sqlalchemy import SQLAlchemy
from app import app

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scheduling.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy object
db = SQLAlchemy(app)

# Define your database models here