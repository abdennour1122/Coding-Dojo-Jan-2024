from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

import re


EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")



class User:
    def __init__(self,data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.password=data["password"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod
    def create(cls,data):
        query="""

            INSERT INTO users(first_name,last_name,email,password)
            VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)
        """
        result=connectToMySQL(DATABASE).query_db(query,data)
    @classmethod
    def get_by_email(cls,data):
        query="""
                SELECT * FROM users 
                where email=%(email)s        
            """
        result=connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return User(result[0])
    
    @classmethod
    def get_by_id(cls,data):
        query="""
                SELECT * FROM users 
                where id=%(id)s        
            """
        result=connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return User(result[0])

    @staticmethod
    def validate_user(data):
        is_valid=True 
        if len(data["first_name"])<1:
            is_valid=False
            flash("first name is required!!!!", "first_name")  

        
    
        if len(data["last_name"])<1:
            is_valid=False
            flash("last name is required!!!!", "last_name")  
        
        if len(data["email"])<1:
            is_valid=False
            flash("email is required!!!!", "email")
        elif not EMAIL_REGEX.match(data["email"]):
            flash("invalid email")
        else:
            email_dict={"email":data["email"]}
            potential_user=User.get_by_email(email_dict)
            if potential_user:
                is_valid=False
                flash("this email is already taken","email")
        if len(data["password"])<1:
            is_valid=False
            flash("password is required!!!!", "password")
        elif not data["password"]==data["confirm_password"]:
            is_valid=False
            flash("password is required!!!!", "confirm_password")


        return is_valid
    @staticmethod
    def validate_login_user(data):
        if len(data["email"])<1:
            is_valid=False
            flash("email is required!!!!", "email")
        elif not EMAIL_REGEX.match(data["email"]):
            flash("invalid email")
        
        if len(data["password"])<1:
            is_valid=False
            flash("password is required!!!!", "password")
