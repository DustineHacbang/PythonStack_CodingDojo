from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:

#set the conditions in the data base for dojo tables
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

#acess the data table and displays the info
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninja').query_db(query)
        dojos = []

        for d in results:
            dojos.append( cls(d) )
        return dojos

#pulls information of a ninja by using the id of the dojo
    @classmethod
    def get_one_with_ninjas(cls, data ):
# querys in to the data table of dojos
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninja').query_db(query,data)
        print(results)
        dojo = cls(results[0])
#sets conditions of the ninjas
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(n) )
        return dojo

#saves the information to the data base
    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninja').query_db(query,data)
        return result
