
# create database tables
users_table = """CREATE TABLE IF NOT EXISTS users
            (
                user_id SERIAL PRIMARY KEY, 
                username VARCHAR(50) NOT NULL,
                email VARCHAR(50),
                phone VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR (300) NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
        )"""


queries = [users_table]