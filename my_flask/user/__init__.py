# -*-coding:utf-8-*-

from flask import Blueprint
from models import User

user = Blueprint('user', __name__, url_prefix='/user')
