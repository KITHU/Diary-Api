from flask import json

class TestUsersEdpoints:
    def test_creat_new_user_pass(self, client, init_db):
        # test app ability to create a new user
        data = {
                'first_name':'mwaniki',
                'last_name':'muriuki',
                'email':'mwaniki.muriuki@gmail.com',
                'password':'1234r'
            }
        response = client.post('api/v1/auth/signup',data=json.dumps(data))
        assert response.status_code == 201

    def test_creat_new_user_fails(self, client, init_db):
        # creating new user fails if any of required fields is left black
        data = {
                'first_name':'mwaniki',
                'last_name':'muriuki',
                'email':'mwaniki.muriuki@gmail.com'
            }
        response = client.post('api/v1/auth/signup',data=json.dumps(data))
        assert response.status_code == 400


    def test_signin_user_pass(self, client, init_db):
        # test app ability to sigin existing user
        #with correct email and password
        data = {
                'email':'mwaniki.muriuki@gmail.com',
                'password':'1234r'
            }
        response = client.post('api/v1/auth/signin',data=data)
        assert response.status_code == 200
    
    def test_signin_user_fails(self, client, init_db):
        # test app ability to sigin existing user
        #with incorrect email or password
        data = {
                'email':'weru.muriuki@gmail.com',
                'password':'1234r'
            }
        response = client.post('api/v1/auth/signin',data=data)
        assert response.status_code == 400
