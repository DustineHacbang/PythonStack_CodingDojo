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
