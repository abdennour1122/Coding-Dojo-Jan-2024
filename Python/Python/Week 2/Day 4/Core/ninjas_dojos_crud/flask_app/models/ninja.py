from flask_app.config.mysqlconnection import connectToMySQL
DATABASE="dojos_and_ninjas_schema"
class ninja:
    def __init__(self, data) :
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query="""
            SELECT * FROM dojos_and_ninjas_schema.ninjas;

        """
        result=connectToMySQL(DATABASE).query_db(query)
        ninjas=[]

        for ninja in result :
            ninjas.append(cls(ninja))
        return ninjas
    
    @classmethod
    def create_ninja(cls,data):
        query="""
            INSERT INTO ninjas(first_name,last_name,age,dojo_id)
            values (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
        """
        result=connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    @classmethod
    def get_ninja_byid(cls,data):
        query="""
            SELECT * FROM ninjas 
            where dojo_id=%(dojo_id)s;
        """
        result=connectToMySQL(DATABASE).query_db(query,data)
        ninjas=[]

        for ninja in result :
            ninjas.append(cls(ninja))
        return ninjas