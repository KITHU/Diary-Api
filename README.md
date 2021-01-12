[![Build Status](https://travis-ci.org/KITHU/Diary-Api.svg?branch=master)](https://travis-ci.org/KITHU/Diary-Api)
[![Coverage Status](https://coveralls.io/repos/github/KITHU/Diary-Api/badge.svg?branch=master)](https://coveralls.io/github/KITHU/Diary-Api?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/ebddd3ad732a5466541f/maintainability)](https://codeclimate.com/github/KITHU/Diary-Api/maintainability)

# My DIARY
> A collection of notes from your life..

### End points:
- **POST** : create user */auth/signup*
- **POST** : login user */auth/signin*
- **POST** : reset password */auth/reset*
- **POST** : activate user */auth/active*

- **GET** : fetch all diaries */mydiary/v1/diaryentries*
- **GET** : fetch diary entry  */mydiary/v1/diaryentries/<int:id>* 
- **POST** : create new diary */mydiary/v1/diaryentries*
- **PUT** : modify specific diary */mydiary/v1/diaryentries/<int:id>*
- **DELETE** : delete specific diary */mydiary/v1/diaryentries/<int:id>*
