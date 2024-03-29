from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import coachs
from flask_app.models import clients
from flask_app.models import users
from flask_app.models import messages
from flask_app.models import sessions

class Sport:
    def __init__(self,data) :
        self.id=data["id"]
        self.name=data["name"]
        self.genres=data["genres"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]


    @classmethod
    def newsport(cls,data):
        query = """
                    insert into sports (name,genres)
                    values(%(name)s,%(genres)s);
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    @classmethod
    def delete_sport(cls,data):
        query="""DELETE FROM sports WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    

    @classmethod
    def get_all_sport(cls):
        query = """
                SELECT * FROM sports;
                """
        results = connectToMySQL(DATABASE).query_db(query)
        all_sports =[]
        for sport in results :
            all_sports.append(cls(sport))
        return all_sports
    
    @classmethod
    def get_sport_infos(cls,data):
        query="""
                    SELECT * FROM sports
                    left join coachs  on coachs.sport_id=sports.id
                    where sports.id=%(id)s; 
                """
        result=connectToMySQL(DATABASE).query_db(query,data)
        this_sport=cls(result[0])
        all_coach=[]
        for each_coach in result:
            coach_dict={**each_coach,
                        "id":each_coach["coachs.id"],
                        "created_at":each_coach["coachs.created_at"],
                        "updated_at":each_coach["coachs.updated_at"]
                        }
            all_coach.append(coachs.Coach(coach_dict))
        this_sport.coachs=all_coach
        return this_sport
    

    @staticmethod
    def validate(data):
        is_valid=True
        if len(data["name"])==0:
            is_valid=False
            flash("name field must be fild ","create")
        
        if len(data["genres"])==0:
            is_valid=False
            flash("genres field must be fild ","create")
        return is_valid

