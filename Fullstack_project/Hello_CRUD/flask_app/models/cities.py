from flask_app.config.mysqlconnection import connectToMySQL
# burger.py
class cities:
    def __init__(self,data):
        #this is where your collunm names will be placed at
        self.id = data['id']
        self.name = data['name']
        self.country_code = data['country_code']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cities"
        results = connectToMySQL('world').query_db(query)
        #results becomes a ***LIST OF DICTONARIES**
        cities = []
        #this for loop is pulling out the dictonaries and looking at it
        for dictonary in results:
            cities.append(cls(dictonary))
        return cities
