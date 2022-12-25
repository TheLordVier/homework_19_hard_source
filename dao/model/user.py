# Импортируем библиотеку Marshmallow и её функции
from marshmallow import Schema, fields
# Импортируем db из файла setup_db.py
from setup_db import db


# Создаём модель User с соответствующими сущностями
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(250))
    role = db.Column(db.String(200))


# Описываем модель Movie в виде класса схемы (сериализация)
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
