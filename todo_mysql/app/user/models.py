from app import db
from ..get_time import get_current_time
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    __password = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=get_current_time)

    def set_password(self, password):
        self.__password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.__password, password)

    # def __init__(self, username, phone, password, create_time):
    #     self.username = username
    #     self.phone = phone
    #     self.password = password
    #     self.create_time = create_time
    #
    # def __repr__(self):
    #     return self.username