from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import coachs
from flask_app.models import clients
from flask_app.models import sports
from flask_app.models import users
from flask_app.models import messages

class Session:
    def __init__(self,data) :
        self.id=data["id"]
        self.title=data["title"]
        self.date=data["date"]
        self.coach_id=data["coach_id"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.coach=coachs.Coach.get_coach_by_id({"id":self.coach_id})



    @classmethod
    def show_all_Sessions(cls):
        query = """
            SELECT * FROM sessions;
        """
        result=connectToMySQL(DATABASE).query_db(query)
        if result:
            all_sessions=[]
            for session in result:
                
                this_session=cls(session)
                all_sessions.append(this_session)
            return all_sessions
        return []
    
    @classmethod
    def get_session_by_id(cls, data):
        query="""
                SELECT * FROM sessions WHERE id=%(id)s;
            """
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def coach_sessions(cls,data):
        query="""SELECT * FROM sessions WHERE coach_id=%(id)s;"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            all_sessions=[]
            for session in result:
                
                this_session=cls(session)
                all_sessions.append(this_session)
            return all_sessions
        return []
    
    @classmethod
    def create_session(cls, data):
        query="""
                INSERT INTO sessions (title, date, coach_id)
                VALUES (%(title)s, %(date)s, %(coach_id)s);
                """
        return connectToMySQL(DATABASE).query_db(query,data)
    

    @classmethod
    def edit_session(cls, data):
        query="""
                update sessions 
                SET title=%(title)s, date=%(date)s
                WHERE id=%(id)s;
                """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete_session(cls, data):
        query="""
                DELETE FROM sessions 
                WHERE id=%(id)s;
                """
        return connectToMySQL(DATABASE).query_db(query,data)