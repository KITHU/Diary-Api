import psycopg2
import datetime

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


"""date getter """
dt=str(datetime.datetime.now().date())


