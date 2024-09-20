import mongoengine as me
from flask_mongoengine import MongoEngine
from .courses import Course

__all__ = ["Course"]


db = MongoEngine()


def init_db(app):
   db.init_app(app)
