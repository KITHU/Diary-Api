from main import bcrypt
import jwt

from api.models.usermodel import UserModel
from api.schema.userschema import UserSchema
from api.middleware.base_validation import ValidationError

userschema = UserSchema()


class Auth():

    def authenticate(self,email,password):
        user = UserModel.get_by_email(email)
        payload = userschema.dump(user)
        if user and self.check_hashed(user.password,password):
            return jwt.encode(payload,'secret').decode('utf-8')
        else:
            raise ValidationError({'message':'invalid email or password'})

    def identity():
        pass
        

    def hash_password(self, raw_pw):
        return bcrypt.generate_password_hash(raw_pw).decode('utf-8')
    
    
    def check_hashed(self, pw_hash, raw_pw):
        return bcrypt.check_password_hash(pw_hash,raw_pw)
