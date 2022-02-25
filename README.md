# KWOLCO FLASK API

Follow the following instructions to run the project:

Download the project code to local machine
CD to the root folder of the project

CD venv,CD Scripts then write activate and press Enter
CD .. then CD.. to the root forder

Run the following command: pip install -r requirements.txt

Once the installation is complete, set up the database.

I have used PostgresSQL For this project.

If you do not have Postgres installed, install to proceed

If you have Postgres, create a new database and name it kwolco_flask

Your database url form database/connection.py on line 8
should follow the following format.


url = 'postgresql://postgres:< database_password >@localhost/< database_name>'

Once the connection is established , now run the app using:

flask run

This will open dev server on port 5000

http://localhost:5000/

Bolow is a postman collection : 

https://documenter.getpostman.com/view/7313595/UVkpPvcH