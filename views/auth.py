# Импортируем фреймворк Flask и его функции
from flask import request
from flask_restx import Resource, Namespace

# Импортируем экземпляр сервиса аутентификация
from implemented import auth_service

# Создаём неймcпейс для представлений
auth_ns = Namespace('auth')


@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        """"
        Аутентификация пользователя (получение токенов)
        """
        request_json = request.json
        username = request_json.get("username")
        password = request_json.get("password")

        if None in [username, password]:
            return "Unauthorized", 401

        tokens = auth_service.generate_tokens(username, password)

        return tokens, 201

    def put(self):
        """"
        Получение новых токенов по refresh_token
        """
        request_json = request.json
        token = request_json.get("refresh_token")
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201
