import os
import psycopg2

from app.database.schemas import queries
from werkzeug.security import generate_password_hash

def dbconnection():
    url = 'postgresql://postgres:kd32479326@localhost/kwolco_flask'
    return psycopg2.connect(url)

def initdb():
    try:
        """
        Try making connection to the db
        
        """
        connection = dbconnection()
        connection.autocommit = True
        #activate cursor and execute queries
        cursor = connection.cursor()
        for query in queries:
            cursor.execute(query)
        connection.commit()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print("Opps! Database Error")
        print(error)
        