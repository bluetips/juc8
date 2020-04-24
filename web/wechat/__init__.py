from flask import Blueprint

wechat = Blueprint('wechat', __name__)

from .views import *
