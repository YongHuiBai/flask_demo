# -*-coding:utf-8-*-
from my_flask import db

class User(db.Model):
    __tablename__ = 'tbl_user'

    id = db.Column(db.Integer, primary_key=True)
    valid = db.Column(db.Boolean, server_default='1')
    created_time = db.Column(db.DateTime, server_default=db.text('CURRENT_TIMESTAMP'))
    last_modified_time = db.Column(db.DateTime, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    nickname = db.Column(db.String(128), unique=True)

    def __repr__(self):
        return '<User %r>' % self.name