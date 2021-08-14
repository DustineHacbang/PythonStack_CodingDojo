from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

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

    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 3:
            flash("first name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if len(user['location']) < 3:
            flash("location must be at least 3 characters.")
            is_valid = False
        if int(user['language']):
            flash("You must select a language")
            is_valid = False
        if len(user['comment']) < 3:
            flash("comment must be at least 3 characters.")
            is_valid = False
        return is_valid