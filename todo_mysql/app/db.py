from flask_sqlalchemy import SQLAlchemy
from .duty_app import app

db = SQLAlchemy(app)