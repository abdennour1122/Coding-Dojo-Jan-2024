from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import coachs
from flask_app.models import sports
from flask_app.models import users
from flask_app.models import messages

from flask_app.models import clients 
class Client:
    def __init__(self,data) :
        self.id=data["id"]
        self.weight=data["weight"]
        self.height=data["height"]
        self.allergies=data["allergies"]
        self.budget=data["budget"]
        self.injury=data["injury"]
        self.trained=data["trained"]
        self.user_id=data["user_id"]
        self.sport_id=data["sport_id"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.details=users.User.get_by_id({'id':self.user_id})

    @classmethod
    def newclient(cls, data):
        query = """
            INSERT INTO clients (weight, height, allergies, budget,injury,trained,user_id,sport_id)
            VALUES (%(weight)s, %(height)s, %(allergies)s, %(budget)s,%(injury)s,%(trained)s,%(user_id)s,%(sport_id)s);
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def request(cls,data):
        query = """
            INSERT INTO requests (session_id,client_id, status)
            VALUES (%(session_id)s,%(client_id)s, 'pending');
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result


    @classmethod
    def delete_client(cls,data):
        query="""DELETE FROM clients WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_client_by__user_id(cls,data):
        query="""
                    SELECT * FROM clients
                    where user_id=%(id)s; 
                """
        result=connectToMySQL(DATABASE).query_db(query,data)
        this_client=cls(result[0])
        return this_client
    
    
    @classmethod
    def get_by_id(cls,data):
        query="""SELECT * FROM clients WHERE id=%(id)s;"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def get_all_clients(cls):
        query="""SELECT * FROM clients;"""
        result=connectToMySQL(DATABASE).query_db(query)
        if result:
            all_clients=[]
            for row in result:
                all_clients.append(cls(row))
            return all_clients
        return []
    
    @classmethod
    def show_all_clients(cls,data):
        pass

    

    # @classmethod
    # def sendreport(cls, data):
    #     query = """
    #         INSERT INTO message_the_admin (sender_id, reciver_id, title, comment)
    #         VALUES (%(sender_id)s, %(reciver_id)s, %(title)s, %(comment)s);
    #     """
    #     sender_id = data["sender_id"]
    #     result = connectToMySQL(DATABASE).query_db(query, data)
    #     return result


    # @classmethod
    # def show_message(cls, user_id):
    #     query = """
    #         SELECT * FROM message_the_admin
    #         WHERE sender_id = %(id)s;
    #     """
    #     # Extract the sender_id from the user_id dictionary directly
    #     sender_id = user_id['id']
    #     # Provide the correct sender_id to the query
    #     result = connectToMySQL(DATABASE).query_db(query, {"id": sender_id})
    #     all_messages = []

    #     for row in result:
    #         this_message = messages.Message(row)
    #         all_messages.append(this_message)

    #     return all_messages


