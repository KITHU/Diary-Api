from flask import Flask
from flask_restplus import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'a7cc3c5ec915dfa1e24267471def9b66'
jwt = JWTManager(app)

import resources

api.add_resource(resources.UserRegistration, '/mydiary/v1/auth/signup')
api.add_resource(resources.UserLogin, '/mydiary/v1/auth/login')
api.add_resource(resources.NewDiaryEntry, '/mydiary/v1/diaryentries')
api.add_resource(resources.get_one_diary_entry, '/mydiary/v1/diaryentries/<int:d_id>')
api.add_resource(resources.del_diary_entry, '/mydiary/v1/diaryentries/<int:d_id>')
api.add_resource(resources.get_all_diary_entries, '/mydiary/v1/diaryentries')
api.add_resource(resources.update_diary_entry, '/mydiary/v1/diaryentries/<int:d_id>')

