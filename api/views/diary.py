from flask import request
from flask_restplus import Resource, reqparse

from main import api
from api.middleware.authentication import Auth

auth = Auth()

@api.route('/diaryentries')
class DiaryAll(Resource):

    @auth.identity
    def get(self):
        return {'message': request.decoded_token}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title',required=True, type=str)
        parser.add_argument('content',required=True, type=str)
        args = parser.parse_args()
        return {'message': args}


@api.route('/diaryentries/<int:id>')
class Diary(Resource):
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title',required=True, type=str)
        parser.add_argument('content',required=True, type=str)
        args = parser.parse_args()
        return {'message': args}
    
    def get(self):
        return {'message': 'return one diary entry for the current user'}
    
    def deletet(self):
        return {'message': 'delete one diary entry for the current user'}
