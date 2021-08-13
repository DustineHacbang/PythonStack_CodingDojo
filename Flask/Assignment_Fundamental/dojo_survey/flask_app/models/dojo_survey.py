from flask_app.config.mysqlconnection import connectToMySQL
# burger.py
class User:
    def __init__(self,data):
        #this is where your collunm names will be placed at
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.location = data['location']
        self.language = data['language']
        self.comment= data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('dojo_survey').query_db(query)
        #results becomes a ***LIST OF DICTONARIES**
        users = []
        #this for loop is pulling out the dictonaries and looking at it
        for dictonary in results:
            users.append(cls(dictonary))
        return users