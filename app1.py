"""mydiary API where users can keep diaries"""

import dbconnection
from models import UserModels as users
from validator import Validate as validate
from jsonhandler import JSONExceptionHandler

from flask import Flask
from flask import jsonify
from flask import request
from flask_restplus import Api
from flask_restplus import model
from flask_restplus import fields
from flask_restplus import Resource
from flask_restplus import reqparse

from flask_jwt_extended import JWTManager
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_raw_jwt
from flask_cors import CORS

from flask_bcrypt import Bcrypt



app = Flask(__name__)
CORS(app)

authorizations = {
    'apikey': {
        'type':'apiKey',
        'schema': 'Bearer',
        'in': 'header',
        'header':'Bearer',
        'name': 'Authorization'
    }
}

api = Api(app, authorizations=authorizations, security='apikey')

app.config['JWT_SECRET_KEY'] = 'a7cc3c5ec915dfa1e24267471def9b66'
jwt = JWTManager(app)

bcrypt = Bcrypt()


#model for signup
signup = api.model('sign up',{
    'username':fields.String(description='name of the user'),
    'email':fields.String(description='email of the user'),
    'password':fields.String(description='password of the user')
})

signup_arg = reqparse.RequestParser()
signup_arg.add_argument('username', type=str,help = 'This field cannot be blank', required = True)
signup_arg.add_argument('email', help = 'This field cannot be blank', required = True)
signup_arg.add_argument('password', help = 'This field cannot be blank', required = True)

#model for login
login = api.model('login',{
    'email':fields.String(description='registered email of the user'),
    'password':fields.String(description='registered password of the user')
})

login_arg = reqparse.RequestParser()
login_arg.add_argument('email', help = 'This field cannot be blank', required = True)
login_arg.add_argument('password', help = 'This field cannot be blank', required = True)


#model for diary entry
new_diary = api.model('diary',{
    'title':fields.String(description='TITLE of the content'),
    'content':fields.String(description='what you have in mind')
})

@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({
        'ok': False,
        'message': 'Missing Authorization Header'
    }), 401

@api.route('/mydiary/v1/auth/signup')
class UserRegistration(Resource):
    """this class handles user signin"""
    @api.expect(signup)
    def post(self):
        """registers user and then users can proceed to login"""
        valid = validate()
        signup = signup_arg.parse_args()
        username = signup['username']
        if(valid.valid_username(username)==False):
            return {"error":"invalid username"},400

        password = signup['password']
        if(valid.valid_username(password)==False):
            return {"error":"password is invalid and week"},400

        email = signup['email']
        if(valid.valid_email(email)==False):
            return {"error":"invalid email andress"},400

        conn = dbconnection.connection()
        cur = conn.cursor()

        cur.execute("SELECT user_email FROM users")
        my_emails = cur.fetchall()
        for emails in my_emails:
            if emails[0] == email:
                return {'error': 'user already exist change credetials'},400
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        cur.execute("""INSERT INTO users(user_name,user_email,password)
                  VALUES (%s, %s, %s)""",[username,email,hashed_password])
        dbconnection.commit_closedb(conn)
        return {"message":"user created successfully"},201

@api.route('/mydiary/v1/auth/login')
class UserLogin(Resource):
    """this class handles user login"""
    @api.expect(login)
    def post(self):
        """log in users and returns a token to user:
        to authorize : Bearer <JWT>"""

        log = login_arg.parse_args()
        password = log['password']
        email = log['email']
        valid = validate()
        if(valid.valid_email(email)==False):
            return {"error":"invalid email andress"},400

        conn = dbconnection.connection()
        cur = conn.cursor()

        cur.execute("SELECT user_email, password FROM users")
        my_emails = cur.fetchall()
        for emails in my_emails:
            if(email == emails[0] and bcrypt.check_password_hash(emails[1],password) == False):
                return {"error":"wrong password" },400
            
            if(email==emails[0] and bcrypt.check_password_hash(emails[1],password) == True):
                access_token = create_access_token(identity = email)
                return {"message":"login successful", "access_token":access_token},201
        return {"error":"invalid login credetials"},404


@api.route('/mydiary/v1/diaryentry')
class get_all_diary_entries(Resource):
    """this class deals with creating a
       and get all diarys"""
    @jwt_required
    @api.expect(new_diary)
    def post(self):
        """this will create a diary entry """
        email = get_jwt_identity()
        valid = validate()
        if not request.json:
            return{"error":"invalid json request"},400
        if not isinstance(request.json['title'],str):
            return {'error':'expect title to be string'},400
        if not isinstance(request.json['content'],str):
            return {'error':'expect content to be string'},400
        conn = dbconnection.connection()
        cur = conn.cursor()
        cur.execute("SELECT user_id FROM users WHERE user_email = (%s)",[email])
        id = cur.fetchone()
        user_id = id[0]
        currentdt = dbconnection.dt

        contentd = request.json['content']
        if(valid.valid_username(contentd) ==False):
            return {"error":"content cannot be null"}

        title = request.json['title']
        if(valid.valid_username(title) ==False):
            return {"error":"title cannot be null"}
        cur.execute("""INSERT INTO diaries(user_id,diary_date,diary_title,diary)
                  VALUES (%s, %s, %s , %s)""",[user_id,currentdt,title,contentd])
        dbconnection.commit_closedb(conn)
        return {'message': "content saved successfully"},201
       
    @jwt_required
    def get(self):
        """this  will return all diary entries"""
        user_email = get_jwt_identity()
        all_diaries = users.get_all_diaries(user_email=user_email)
        return all_diaries

@api.route('/mydiary/v1/diaryentry/<int:d_id>')
class update_diary_entry(Resource):
    """this class updates,fetches one and deletes"""
    @api.expect(new_diary)
    @jwt_required
    def put(self,d_id):
        """update a diary"""
        user_email = get_jwt_identity()
        user_update = users.update_diary(user_email=user_email,d_id=d_id)
        return user_update
    
    @jwt_required
    def get(self,d_id):
        """this method will return one diary entry"""
        user_email = get_jwt_identity()
        get_a_diary = users.get_one_diary(user_email=user_email,d_id=d_id)
        return get_a_diary

    @jwt_required
    def delete(self,d_id):
        """this will delete one diary entry"""
        conn = dbconnection.connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM diaries WHERE diary_id = (%s)",[d_id])
        dbconnection.commit_closedb(conn)
        return {'message': 'deleted'}

    @app.errorhandler(404)
    def error_404(error=None):  # pylint: disable=unused-variable
        # pylint: disable=unused-argument
        """ handle request for unavailable url """
        message = {
            'status': '404',
            'message': request.url + ' Was not found in this server',
        }
        response = jsonify(message)
        response.status_code = 404
        return response

    @app.errorhandler(500)
    def server_error(error=None):  # pylint: disable=unused-argument
        # pylint: disable=unused-variable
        """ handle server error """
        response = {"status": 500, "Message":"Something went wrong!"}
        return response, 500

    @app.errorhandler(405)
    def method_not_allowed(error=None): # pylint: disable=unused-variable
        # pylint: disable=unused-argument
        """ handle method not allowed """
        response = {"status": 405, "Message":"Method not allowed"}
        return response, 405

  

    
   

if __name__ == '__main__':
    app.run(debug=True)