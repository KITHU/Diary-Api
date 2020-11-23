class TestUsersEdpoints:
    def test_creat_new_user(self, client, db):
        data = {
                "first_name":"mwaniki",
                "last_name":"muriuki",
                "email":"mwaniki.muriuki@gmail.com",
                "password":"1234r"
            }
        response = client.post('api/v1/auth/signin', data=data)
        import pdb; pdb.set_trace()
        print(response.status)
        print("+++"*300)