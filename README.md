# Diary_EndPoint

## Rest Endpoints for my diary app

## FEATURES:
- POST endpoint: create user            /mydiary/v1/auth/signup
- POST endpoint: login user             /mydiary/v1/auth/login
- GET endpoint: fetch all diaries       /mydiary/v1/diaryentry
- GET endpoint: fetch one diary         /mydiary/v1/diaryentry/<int:id> 
- POST endpoint: create new diary       /mydiary/v1/diaryentry
- PUT endpoint: modify one diary        /mydiary/v1/diaryentry/<int:id>
- DELETE endpoint: delete one diary     /mydiary/v1/diaryentry/<int:id>


## HOW TO TEST API ONLINE
- The api can be tested online or on localhost
- visit : https://tranquil-spire-14325.herokuapp.com

## TEST API ON LOCAL MACHINE
- clone git repo : https://github.com/KITHU/Diary_EndPoint.git

## REQUIREMENTS:
- python three installed
- virtual environment
- install requirements.txt

## HOW TO RUN IT:
- run the script in script.py to create database table localy
- on dbconnection.py comment out heroko connection
- start server : python app1.py
- go to the given url and test or postman
    
## HOW TO TEST ENDPOINTS:
## create user
- create user endpoint requires username, email and password
- this data should be a valid json object submited as body
- {"username":"name","email":"user email","password":"password"}

## login user
- login endpoint requires email and password
- this data should be a valid json object submited as body
- {"email":"user email","password":"password"}

## login user
- login endpoint requires email and password
- this data should be a valid json object submited as body
- {"email":"user email","password":"password"}

## create diary and modify diary
- require title and content
- this data should be a valid json object submited as body
- {"title":"ur title","content":"write something"}

## create diary and modify diary
- require title and content
- this data should be a valid json object submited as body
- {"title":"ur title","content":"write something"}

## other endpoints
- delete requires the id of the diary entry
- get all endpoint returns all diaries


