from flask_app.config.mysqlconnection import connectToMySQL
DATABASE="dojos_and_ninjas_schema"
class dojo:

    def __init__(self, data) :
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query="""
            SELECT * FROM dojos_and_ninjas_schema.dojos;

        """
        result=connectToMySQL(DATABASE).query_db(query)
        dojos=[]

        for dojo in result :
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def create_dojo(cls,data):
        query="""
            INSERT INTO dojos(name)
            values (%(name)s);
        """
        result=connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    @classmethod
    def get_dojo_byid(cls,data):
        query="""
            SELECT * FROM dojos 
            where id=%(id)s;
        """
        result=connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<0:
            return False
        else:
            return cls(result[0])

     

        