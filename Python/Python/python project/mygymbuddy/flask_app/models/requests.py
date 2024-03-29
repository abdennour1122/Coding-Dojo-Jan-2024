from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import clients
from flask_app.models import sports
from flask_app.models import users
from flask_app.models import coachs
from flask_app.models import sessions

class Request:
    def __init__(self,data) :
        self.id=data["id"]
        self.session_id=data["session_id"]
        self.client_id=data["client_id"]
        self.client=clients.Client.get_by_id({'id':self.client_id})
        self.session=sessions.Session.get_session_by_id({'id':self.session_id})
        self.status=data["status"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod
    def update_status(cls, data):
        query="""
                UPDATE requests SET status=%(status)s WHERE id=%(id)s;
                """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def update_session(cls, data):
        query="""
                UPDATE requests SET title=%(title)s, date=%(date)s;
                """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_coach_all_requests(cls, data):
        query="""
                select * from coachs
                join sessions on sessions.coach_id=coachs.id
                join requests on sessions.id= requests.session_id
                join clients on clients.id=requests.client_id
                where coachs.id=%(id)s;
                """
        result= connectToMySQL(DATABASE).query_db(query,data)
        if result:

            this_coach=coachs.Coach(result[0])
            all_sessions=[]
            all_requests=[]
            all_clients=[]
            for row in result:
                session_dict={
                    **row,
                    "id": row['sessions.id'],
                    "created_at": row['sessions.created_at'],
                    "updated_at": row['sessions.updated_at'],
                }
                all_sessions.append(sessions.Session(session_dict))
                request_dict={
                    **row,
                    "id": row['requests.id'],
                    "created_at": row['requests.created_at'],
                    "updated_at": row['requests.updated_at'],
                }
                all_requests.append(cls(request_dict))
                client_dict={
                    **row,
                    "id": row['clients.id'],
                    "user_id": row['clients.user_id'],
                    "sport_id": row['clients.sport_id'],
                    "created_at": row['clients.created_at'],
                    "updated_at": row['clients.updated_at'],
                }
                all_clients.append(clients.Client(client_dict))
            this_coach.sessions= all_sessions
            this_coach.requests=all_requests
            this_coach.clients=all_clients
            return this_coach
        return False



        
