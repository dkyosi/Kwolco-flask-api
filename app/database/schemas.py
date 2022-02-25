
# create database tables
users_table = """CREATE TABLE IF NOT EXISTS users
            (
                user_id SERIAL PRIMARY KEY, 
                username VARCHAR(50) NOT NULL UNIQUE,
                email VARCHAR(50),
                phone VARCHAR(50) NOT NULL,
                password VARCHAR (300) NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
        )"""

countries_table = """CREATE TABLE IF NOT EXISTS countries
                        (
                                country_id SERIAL PRIMARY KEY,
                                country_name VARCHAR(50) NOT NULL UNIQUE,
                                population BIGINT NOT NULL,
                                continent VARCHAR NOT NULL,
                                created_at TIMESTAMP DEFAULT NOW()
                        )"""


products_table = """CREATE TABLE IF NOT EXISTS products
                        (
                                product_id SERIAL PRIMARY KEY,
                                country_id INT,
                                product_name VARCHAR(50) NOT NULL,
                                tones BIGINT NOT NULL,
                                price_per_kg BIGINT NOT NULL,
                                created_at TIMESTAMP DEFAULT NOW(),
                                FOREIGN KEY(country_id)REFERENCES countries(country_id),
                                CONSTRAINT product_country_unique UNIQUE (product_name, country_id)
                        )"""


queries = [users_table, countries_table, products_table]
