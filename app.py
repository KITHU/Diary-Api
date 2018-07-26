from flask_restplus import Api,model,fields
from flask_jwt_extended import JWTManager
from flask_restplus import Resource, reqparse,Api
import dbconnection

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_raw_jwt
from flask_bcrypt import Bcrypt


app = Flask(__name__)




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


@api.route('/mydiary/v1/auth/signup')
class UserRegistration(Resource):
    @api.expect(signup)
    def post(self):
        """registers user and then users can proceed to login"""
        signup = signup_arg.parse_args()
        username = signup['username']
        password = signup['password']
        email = signup['email']

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
    @api.expect(login)
    def post(self):
        """log in users and returns a token to user:
        to authorize : Bearer <JWT>"""
        log = login_arg.parse_args()
        password = log['password']
        email = log['email']

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
    @jwt_required
    @api.expect(new_diary)
    def post(self):
        """this will create a diary entry """
        email = get_jwt_identity()
        if not request.json:
            return{"ty":"error"},400
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
        title = request.json['title']

        cur.execute("""INSERT INTO diaries(user_id,diary_date,diary_title,diary)
                  VALUES (%s, %s, %s , %s)""",[user_id,currentdt,title,contentd])
        dbconnection.commit_closedb(conn)
        return {'message': "content saved successfully"},201
       
    @jwt_required
    def get(self):
        """this  will return all diary entries"""
        conn = dbconnection.connection()
        cur = conn.cursor()
        user_email = get_jwt_identity()

        cur.execute("SELECT user_id FROM users WHERE user_email = (%s)",[user_email])
        id = cur.fetchone()
        user_id = id[0]
        cur.execute("SELECT diary_id,diary_date,diary_title,diary FROM diaries WHERE user_id = (%s)",[user_id])
        diaries = cur.fetchall()
        user_diaries = []
        for diary in diaries:
            user_diary={"diary_id":diary[0],"date_written":diary[1],"title":diary[2],"content":diary[3]}
            user_diaries.append(user_diary)
        dbconnection.commit_closedb(conn)
        return {'user diaries': user_diaries},200

@api.route('/mydiary/v1/diaryentry/<int:d_id>')
class update_diary_entry(Resource):
    @api.expect(new_diary)
    @jwt_required
    def put(self,d_id):
        """update a diary"""
        user_email = get_jwt_identity()
        conn = dbconnection.connection()
        cur = conn.cursor()
        cur.execute("SELECT user_id FROM users WHERE user_email = (%s)",[user_email])
        id = cur.fetchone()
        user_id = id[0]
        cur.execute("SELECT diary_title,diary FROM diaries WHERE diary_id = (%s) AND user_id = (%s)",[d_id,user_id])
        diary=cur.fetchone()
        if(diary == None):
            return {"message":"invalid id or you have no diary entries"},400
        if not request.json:
            return{"ty":"error"},400
        if not isinstance(request.json['title'],str):
            return {'error':'expect title to be string'},400
        if not isinstance(request.json['content'],str):
            return {'error':'expect content to be string'},400
        contentd = request.json['content']
        title = request.json['title']
        cur.execute("UPDATE diaries SET diary_title = (%s), diary = (%s) WHERE diary_id = (%s)",[title,contentd,d_id])
        dbconnection.commit_closedb(conn)
        return {"message":"updated"}
    
    @jwt_required
    def get(self,d_id):
        """this method will return one diary entry"""
        conn = dbconnection.connection()
        cur = conn.cursor()
        user_email = get_jwt_identity()
        cur.execute("SELECT user_id FROM users WHERE user_email = (%s)",[user_email])
        id = cur.fetchone()
        user_id = id[0]
        cur.execute("SELECT diary_id,diary_date,diary_title,diary FROM diaries WHERE diary_id = (%s) AND user_id = (%s)",[d_id,user_id])
        diaries = cur.fetchone()
        if(diaries ==None):
            return {'diary': "YOU HAVE ZERO DIARIES ADD SOME"},200
        diary={"diary_id":diaries[0],"date":diaries[1],"title":diaries[2],"content":diaries[3]}
        dbconnection.commit_closedb(conn)
        return {'diary': diary},200

    @jwt_required
    def delete(self,d_id):
        """this will delete one diary entry"""
        conn = dbconnection.connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM diaries WHERE diary_id = (%s)",[d_id])
        dbconnection.commit_closedb(conn)
        return {'message': 'deleted'}
    
   

if __name__ == '__main__':
    app.run(debug=True)