# -*-coding:utf-8-*-
from flask import Blueprint
from flask_restful import Api
from resources import users

user = Blueprint('user', __name__, url_prefix='/user')
api = Api(user)

api.add_resource(users.UserInfo, '/user_info')