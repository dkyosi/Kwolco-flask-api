import re

def valid_user_field(username):
        """validate user field"""
        regex = "^[a-zA-Z0-9]{3,}$"
        return re.match(regex, str.strip(username))

def validate_data_signup(args):
    """validate user details"""
    try:
        if " " in args["email"]:
            return{
                "status": 401,
                "error": "Email should be one word, no spaces"
                }, 401
        elif args["email"] == '' or \
             args["password"] == '' or args["password"].isspace() or \
             args["confirm"] == '':
                return{
                    "status": 401,
                    "error": "Check if either of the field is left unfilled"
                    }, 401

        elif len(args['password'].strip()) < 5:
            return{
                    "status": 401,
                    "error": "Password should have atleast 5 characters"
                    }, 401
        elif args['password'] != args['confirm']:
            return{
                    "status": 401,
                    "error": "Passwords do not match"
                    }, 401
        elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", args["email"]):
            return{
                    "status": 401,
                    "error": "Invalid email provided"
                    }, 401
        elif len(args["password"]) < 6 or len(["password"]) > 12:
            return{
                    "status": 401,
                    "error": "Password length should be between 6 and 12 characters long"
                    }, 401
        else:
            return "valid"
    except Exception as error:
        return{
                    "status": 401,
                    "error": "please provide all the fields, missing " + str(error)
                    }, 401