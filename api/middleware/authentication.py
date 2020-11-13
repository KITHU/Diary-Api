from main import bcrypt


class Auth():
    
    def authenticate():
        pass

    @classmethod
    def hash_password(cls, raw_pw):
        return bcrypt.generate_password_hash(raw_pw).decode('utf-8')

    def check_hashed(self, pw_hash, raw_pw):
        return bcrypt.check_password_hash(pw_hash,raw_pw)
