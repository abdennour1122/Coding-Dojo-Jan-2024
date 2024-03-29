from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import coachs
from flask_app.models import clients
from flask_app.models import sports
from flask_app.models import messages
from flask_app.models import sessions
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self,data) :
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.role=data["role"]
        self.age=data["age"]
        self.phone=data["phone"]
        self.password=data["password"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]


    @classmethod
    def get_by_id(cls,data):
        query="""SELECT * FROM users WHERE id=%(id)s;"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return None
    
    @classmethod
    def get_by_email(cls,data):
        query="""SELECT * FROM users WHERE email=%(email)s;"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return False
    


        #* =========== READ ALL ===========
    @classmethod
    def show_all_coachs(cls):
        query = """
        SELECT * FROM coachs;
        """
        result=connectToMySQL(DATABASE).query_db(query)
        all_coachs=[]
        for each_user in result:
            this_coach=coachs.Coach(each_user)
            all_coachs.append(this_coach)
        return all_coachs
    

    @classmethod
    def show_all_clients(cls):
        query = """
        SELECT * FROM clients;
        """
        result=connectToMySQL(DATABASE).query_db(query)

        all_clients=[]
        if result:
            for each_user in result:
                this_client=clients.Client(each_user)
                all_clients.append(this_client)
        return all_clients
    
   
    
    
    
    @classmethod
    def show_all_sports(cls):
        query = "SELECT * FROM sports;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_sport = []
        if results :
            for row in results:
                this_sport=sports.Sport(row)
                all_sport.append(this_sport)
            return all_sport
        return []
    
    @classmethod
    def show_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_users = []
        if results :
            for row in results:
                this_user=cls(row)
                all_users.append(this_user)
            return all_users
        return []
    
    

    
    # @classmethod
    # def delete_message(cls,data):
    #     query="""DELETE FROM messages WHERE id=%(id)s;"""
    #     return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete_user(cls,data):
        query="""DELETE FROM users WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)

    
        
    @classmethod
    def newuser(cls,data):
        query = """
                    insert into users (first_name,last_name,email,role,age,phone,password)
                    values(%(first_name)s,%(last_name)s,%(email)s,%(role)s,%(age)s,%(phone)s,%(password)s);
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    

    @staticmethod
    def validate_user(data):
        is_valid=True
        # first & lastname validation
        if len(data["first_name"])==0:
            is_valid=False
            flash("First Name field must be fild ","create")
        
        if len(data["last_name"])==0:
            is_valid=False
            flash("Last Name field must be fild ","create")
        if len(data["age"])==0:
            is_valid=False
            flash("Ager field must be fild ","create")


        # email validation
        # email pattern:regex
        if len(data["email"])==0:
            is_valid=False
            flash("email field must be fild ","create")

        if not EMAIL_REGEX.match(data['email']):
            flash("invalid email address","create")
            is_valid=False
        #email must be unique
        if User.get_by_email({'email':data['email']}):
            flash("Email already in use, hope by you","create")
            is_valid=False
        if len(data["phone"])!=8:
            flash("phone number too short","create")
            is_valid=False
        #password
        # password length
        if len(data["password"])<6:
            flash("Password too short","create")
            is_valid=False
        # compare password and confirm password
        elif data["password"]!=data["confirm_password"]:
            flash("Password must match","create")
            is_valid=False
        return is_valid
    
    
    @staticmethod
    def validate_login_user(data):
        is_valid = True

        if len(data["email"]) < 1:
            is_valid = False
            flash("email is required !", "email")
        # test whether a field matches the pattern
        elif not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address!", "email")
            is_valid = False

        if len(data["password"]) < 1:
            is_valid = False
            flash("password is required !", "password")

        return is_valid


