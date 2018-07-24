import psycopg2

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
