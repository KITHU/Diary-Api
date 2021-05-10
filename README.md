[![Build Status](https://travis-ci.org/KITHU/Diary-Api.svg?branch=master)](https://travis-ci.org/KITHU/Diary-Api)
[![Coverage Status](https://coveralls.io/repos/github/KITHU/Diary-Api/badge.svg?branch=master)](https://coveralls.io/github/KITHU/Diary-Api?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/ebddd3ad732a5466541f/maintainability)](https://codeclimate.com/github/KITHU/Diary-Api/maintainability)

# **My DIARY**
> A collection of notes from your life..

## **Set Up Development Environment:**
- Clone the Diary-Api repo and cd into it:
  ```
   https://github.com/KITHU/Diary-Api.git 
  ```
- Install all Dependancies
  ```
   pipenv install 
  ```

- Make a copy of the .env.sample file and rename it to .env and update the variables accordingly
- Activate a virtual environment:
  ```
    pipenv shell
  ```
- Apply migrations:
  ```
    flask db upgrade

  ```
- Make migrations:
  ```
    flask db migrate

  ```

- Run App
  ```
    python manage.py runserver
             or 
    flask run
  ```

- Run Tests
  ```
    pytest
  ```

## **Endpoints:**
### SignUp

`POST /api/v1/auth/signup`

Example request body:
``` 
{
    "first_name":"John",
    "last_name":"Doe",
    "email":"johndoe@gmail.com",
    "password":"djnoe12"
}

```

### SignIn

`POST /api/v1/auth/signin`

Example request body:
``` 
{
    "email":"johndoe@gmail.com",
    "password":"djnoe12"
}

```

- **POST** : reset password */auth/reset*
- **POST** : activate user */auth/active*

- **GET** : fetch all diaries */mydiary/v1/diaryentries*
- **GET** : fetch diary entry  */mydiary/v1/diaryentries/<int:id>* 
- **POST** : create new diary */mydiary/v1/diaryentries*
- **PUT** : modify specific diary */mydiary/v1/diaryentries/<int:id>*
- **DELETE** : delete specific diary */mydiary/v1/diaryentries/<int:id>*
