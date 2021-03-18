from flask_restful import Resource, http_status_message
from flask import request
from models.user import UserModel


class UserSignup(Resource):
    """
    User Signup resource, will manage all the user registrations
    """
    def __init__(self, **kwargs):
        self.secret_key = kwargs['secret_key']

    def post(self):
        """
        Register a new user.

        :return: the token for the user that has been created, or an message.
        """
        json_data = request.form
        if 'username' in json_data and 'password' in json_data:
            username = json_data['username']
            password = json_data['password']
            user = UserModel.query.filter_by(username=username).first()
            if not user:
                user = UserModel(username=username, password=password)
                user.create()
                response = {"token": user.generate_auth_token(secret_key=self.secret_key)}
                http_code = 201
            else:
                response = "User already exists"
                http_code = 403
        else:
            http_code = 400
            response = http_status_message(http_code)

        return response, http_code


class UserLogin(Resource):
    """
    User Login resource, will manage all the user logged in actions.
    """
    def __init__(self, **kwargs):
        self.secret_key = kwargs['secret_key']

    def post(self):
        """
        User log in.

        :return: the token for the user that has been created, or an message.
        """
        json_data = request.form
        if 'username' in json_data and 'password' in json_data:
            username = json_data['username']
            password = json_data['password']
            user = UserModel.query.filter_by(username=username).first()
            if user:
                if user.verify_password(password):
                    http_code = 200
                    response = {"token": user.generate_auth_token(secret_key=self.secret_key)}
                else:
                    http_code = 401
                    response = http_status_message(http_code)
            else:
                http_code = 401
                response = http_status_message(http_code)
        else:
            http_code = 400
            response = http_status_message(http_code)

        return response, http_code
