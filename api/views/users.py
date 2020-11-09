from flask import request
from flask_restplus import Resource, reqparse
from marshmallow import ValidationError

from main import api
from api.schema.userschema import UserSchema

userschema = UserSchema()

@api.route('/auth/login')
class Login(Resource):
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email',required=True, type=str)
        parser.add_argument('password',required=False, type=int)
        args = parser.parse_args()
        return {'message': args}


@api.route('/auth/signup')
class SignUp(Resource):
    def post(self):
        try:
            user_data = userschema.load(request.get_json())
        except ValidationError as err:
            return err.messages,400
        return {'message': user_data}, 201


@api.route('/auth/confirm')
class Confirm(Resource):
    def post(self):
        return {'message': 'confirm user and activate them'}


@api.route('/auth/reset')
class Reset(Resource):
    def post(self):
        return {'message': 'reset user password'}
