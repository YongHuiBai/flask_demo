# -*-coding:utf-8-*-
from flask_restful import Resource

class UserInfo(Resource):
    def get(self):
        return '老爷是傻逼'