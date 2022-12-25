# Импортируем фреймворк Flask и его функции
from flask import request
from flask_restx import Resource, Namespace

# Импортируем схему пользователя
from dao.model.user import UserSchema
# Импортируем экземпляр сервиса пользователь
from implemented import user_service

# Создаём неймcпейс для представлений
user_ns = Namespace('users')

# Cоздаём экземпляры схем
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route("/")
class UsersView(Resource):
    def get(self):
        """"
        Получение списка всех сущностей (пользователь)
        """
        users = user_service.get_all()
        result = users_schema.dump(users)
        return result, 200

    def post(self):
        """"
        Создание определённой сущности (пользователь)
        """
        request_json = request.json
        user = user_service.create(request_json)
        return "User created", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid: int):
        """"
        Получение конкретной сущности по идентификатору (пользователя)
        """
        try:
            user = user_service.get_one(uid)
            return user_schema.dump(user), 200
        except Exception as e:
            return str(e), 404

    def put(self, uid: int):
        """"
        Обновление конкретной сущности по идентификатору (пользователя)
        """
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = uid
        user_service.update(request_json)
        return "User updated", 204

    def delete(self, uid: int):
        """"
        Удаление конкретной сущности по идентификатору (пользователя)
        """
        user_service.delete(uid)
        return "User deleted", 204
