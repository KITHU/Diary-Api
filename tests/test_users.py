class TestUsersEdpoints:
    def test_creat_new_user(self, client, init_db):
        data = {
                "first_name":"mwaniki",
                "last_name":"muriuki",
                "email":"mwaniki.muriuki@gmail.com",
                "password":"1234r"
            }
        response = client.post('api/v1/auth/signup', data=data)