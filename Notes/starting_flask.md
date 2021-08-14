1. create folder 

2. install flask & pymysql
    ```
    python -m pipenv install flask pymysql

    ```

3. lunch shell
    ```
    pinenv shell
    ```

4. create folder structor
    - server.py
    - flask_app
        - templates 
        - config
            - mysqlconnection.py
        - controllers
            - {name of table}.py
        - models
            - {name of table}.py
        - static
            - css folder
                - style.css
            - js folder
                - script.js
            - img folder
        -_init_.py

5. server.py
```py
# Import Flask to allow us to create our app
from flask_app import app  
from flask_app.controllers import users
# Ensure this file is being run directly and not from a different module    
if __name__=="__main__":  
 # Run the app in debug mode.     
    app.run(debug=True)   


```


6. mysqlconnection.py
```py
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
# change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
# establish the connection to the database
        self.connection = connection
# the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
# INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
# SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
# UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
# if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
# close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
```

7. controller

    the controller is where all your routes are stored
```py

from flask_app import app
from flask import render_template,redirect,request,session,flash
#from {model_folder} import {model_file}

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html') 

```

8. models
models file is where database communications are "queries queries"
    
```py
    from flask_app.config.mysqlconnection import connectToMySQL
# burger.py
class Burger:
    def __init__(self,data):
        #this is where your collunm names will be placed at
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM {name_of_table}"
        results = connectToMySQL('{name_of_the_data_base}').query_db(query)
        #results becomes a ***LIST OF DICTONARIES**
        {name_of_table} = []
        #this for loop is pulling out the dictonaries and looking at it
        for dictonary in results:
            {name_of_table}.append(cls(dictonary))
        return {name_of_table}



```

9. \_\_init__.py
```py

# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"

```


        