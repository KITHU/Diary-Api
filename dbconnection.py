""""function to connect to database"""
import datetime
import psycopg2

# def connection():
#     """establish connection to database """
#     try:
#         conn = psycopg2.connect(
#             database='d7f3q9oc94flbp',
#             user='eurwbxjvautgcf',
#             host='ec2-23-23-242-163.compute-1.amazonaws.com',
#             password='4497fbe94664feb676f14fbbc38d90d910563bb0b54c82ee99c099dab5fb2a84'
#             )
#     except: # pylint: disable=bare-except
#         print("I am unable to connect to the database")
#     return conn

# def commit_closedb(dbconn):
#     "used to close and commit changes"
#     dbconn.commit()
#     dbconn.close()

dt = str(datetime.datetime.now().date()) # pylint: disable=invalid-name


def connection():
    """establish connection to database """
    try:
        conn = psycopg2.connect("dbname='my_diary' user='root' host='localhost' password='root2'")
    except:
        print("I am unable to connect to the database")
    print("connected")
    return conn

def commit_closedb(dbconn):
    dbconn.commit()
    dbconn.close()
