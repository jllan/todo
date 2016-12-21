from ..db import db
from ..get_time import get_current_time

# class Category(db.Model):
#     __tablename__ = "category"
#     category_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return self.name


class Duty(db.Model):
    __tablename__ = "duty"
    id = db.Column(db.Integer, primary_key=True)
    # category_id = db.Column(db.Integer, unique=True)
    title = db.Column(db.String(64), unique=True, nullable=False)
    status = db.Column(db.Integer, default=0)
    is_show = db.Column(db.Integer, default=1)
    create_time = db.Column(db.DateTime, default=get_current_time)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    author = db.relationship('User', backref=db.backref('duty', lazy='dynamic'), uselist=False)