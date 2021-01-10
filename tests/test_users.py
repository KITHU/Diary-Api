from flask import json

class TestUsersEdpoints:
    def test_creat_new_user(self, client, init_db):
        data = {
                'first_name':'mwaniki',
                'last_name':'muriuki',
                'email':'mwaniki.muriuki@gmail.com',
                'password':'1234r'
            }
        response = client.post('api/v1/auth/signup',data=json.dumps(data))
        assert response.status_code == 201


    def test_signin_user(self, client, init_db):
        data = {
                'email':'mwaniki.muriuki@gmail.com',
                'password':'1234r'
            }
        response = client.post('api/v1/auth/signin',data=data)
        assert response.status_code == 200
