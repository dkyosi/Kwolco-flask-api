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
        """Seed countries to database"""
        gen_countries = """
                INSERT INTO
                countries (country_name, population, continent)
                VALUES ('KENYA', '47000000', 'Africa')
                ON CONFLICT (country_name) DO NOTHING;
                INSERT INTO
                countries (country_name, population, continent)
                VALUES ('TANZANIA', '40000000', 'Africa')
                ON CONFLICT (country_name) DO NOTHING;
                INSERT INTO
                countries (country_name, population, continent)
                VALUES ('UGANDA', '46000000', 'Africa')
                ON CONFLICT (country_name) DO NOTHING;
                INSERT INTO
                countries (country_name, population, continent)
                VALUES ('ETHIOPIA', '50000000', 'Africa')
                ON CONFLICT (country_name) DO NOTHING;
                INSERT INTO
                countries (country_name, population, continent)
                VALUES ('RWANDA', '30000000', 'Africa')
                ON CONFLICT (country_name) DO NOTHING;
                """
        connection = dbconnection()
        cursor = connection.cursor()
        cursor.execute(gen_countries)
        connection.commit()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print("Opps! Database Error")
        print(error)
        