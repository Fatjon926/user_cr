from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name='user_cr'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        if results:
        # Iterate over the db results and create instances of friends with cls.
            for user in results:
                users.append( cls(user) )
            return users
        return users

    @classmethod
    def save(cls,data):
        query="insert into users (first_name,last_name,email) values ( %(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)
