from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import clients
from flask_app.models import sports
from flask_app.models import users
from flask_app.models import messages
from flask_app.models import sessions
from flask_app.models import requests

class Coach:
    def __init__(self,data) :
        self.id=data["id"]
        self.certifcat=data["certifcat"]
        self.experience=data["experience"]
        self.sport_id=data["sport_id"]
        self.user_id=data["user_id"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.details=users.User.get_by_id({'id':self.user_id})



        
    @classmethod
    def newcoach(cls,data):
        query = """
                    insert into coachs (certifcat,experience,sport_id,user_id)
                    values(%(certifcat)s,%(experience)s,%(sport_id)s,%(user_id)s);
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    

        
    
    @classmethod
    def get_all_requests(cls,data):
        query="""SELECT * FROM requests WHERE session_id=%(id)s;"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            all_requests=[]
            for row in result:
                all_requests.append(requests.Request(row))
            return all_requests
        return []
    
    @classmethod
    def get_all_coachs(cls):
        query="""SELECT * FROM coachs;"""
        result=connectToMySQL(DATABASE).query_db(query)
        if result:
            all_coachs=[]
            for row in result:
                all_coachs.append(cls(row))
            return all_coachs
        return []
    
    @classmethod
    def get_coach_by__user_id(cls,data):
        query="""
                    SELECT * FROM coachs
                    where user_id=%(id)s; 
                """
        result=connectToMySQL(DATABASE).query_db(query,data)
        this_coach=cls(result[0])
        return this_coach
    
    @classmethod
    def get_coach_by_id(cls,data):
        query="""
                    SELECT * FROM coachs
                    where id=%(id)s; 
                """
        result=connectToMySQL(DATABASE).query_db(query,data)
        this_coach=cls(result[0])
        return this_coach
    

    @classmethod
    def delete_coach(cls,data):
        query="""DELETE FROM coachs WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @staticmethod
    def validate_coach(data):
        is_valid=True
        if len(data["certifcat"])==0:
            is_valid=False
            flash("certifcat field must be fild ","create")
        
        if len(data["experience"])==0:
            is_valid=False
            flash("experience field must be fild ","create")
        return is_valid
