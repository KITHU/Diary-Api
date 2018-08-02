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
            return{"error":"invalidy json body"},400
        data = request.json
        contentd = data.get('content')
        title = data.get('title')

        if not contentd and not title:
            return {"error":"check your input data"},400
        
        if contentd and title:
            valid=validate()
            if(valid.valid_title(title)==False):
                return {"error":"Enter valid title"},400
            if(valid.valid_title(contentd)==False):
                return {"error":"Enter valid content"},400 
            cur.execute("UPDATE diaries SET diary_title = (%s), diary = (%s) WHERE diary_id = (%s)", [title,contentd,d_id])
            dbconnection.commit_closedb(conn)
            return {"message":"all updated"}

        if contentd:
            valid=validate()
            if(valid.valid_title(contentd)==False):
                return {"error":"Enter valid content"},400
            cur.execute("UPDATE diaries SET diary = (%s) WHERE diary_id = (%s)", [contentd,d_id])
            dbconnection.commit_closedb(conn)
            return {"message":"content updated"}
        
        if title:
            valid=validate()
            if(valid.valid_title(title)==False):
                return {"error":"Enter valid content"},400
            cur.execute("UPDATE diaries SET diary_title = (%s) WHERE diary_id = (%s)", [title,d_id])
            dbconnection.commit_closedb(conn)
            return {"message":"title updated"}

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