import dbconnection
from flask_restplus import reqparse
from flask_restplus import Api
from flask_restplus import model
from validator import Validate as validate
from flask import Flask
from flask import jsonify
from flask import request
class UserModels():
    @staticmethod
    def update_diary(user_email,d_id):
        """update one diary via id passed"""
        conn = dbconnection.connection()
        cur = conn.cursor()
        cur.execute("SELECT user_id FROM users WHERE user_email = (%s)",[user_email])
        id = cur.fetchone()
        user_id = id[0]
        cur.execute("SELECT diary_title,diary FROM diaries WHERE diary_id = (%s) AND user_id = (%s)",[d_id,user_id])
        diary=cur.fetchone()
        if(diary == None):
            return {"error":"invalid id or you have no diary entries"},400
        if not request.json:
            return{"error":"ivalidy json body"},400
        if not request.json['content']:
            return {"error":"content field is required"},400
        if not request.json['title']:
            return {"error":"title field is required"},400
        if not isinstance(request.json['title'],str):
            return {'error':'expect title to be string'},400
        if not isinstance(request.json['content'],str):
            return {'error':'expect content to be string'},400

        valid=validate()
       
        contentd = request.json['content']
        if(valid.valid_title(contentd)==False):
            return {"error":"Enter valid content"},400
        
        title = request.json['title']
        if(valid.valid_title(title)==False):
            return {"error":"Enter valid title"},400
        
        cur.execute("UPDATE diaries SET diary_title = (%s), diary = (%s) WHERE diary_id = (%s)", [title,contentd,d_id])
        dbconnection.commit_closedb(conn)
        return {"message":"updated"}


    @staticmethod
    def get_one_diary(user_email,d_id):
        conn = dbconnection.connection()
        cur = conn.cursor()
        
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
  
    @staticmethod
    def get_all_diaries(user_email):
        conn = dbconnection.connection()
        cur = conn.cursor()
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
        return {'diaries': user_diaries},200