from mysqlconnection import connectToMySQL

class User:
    DB = "users_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"

        results = connectToMySQL(cls.DB).query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, user_id):
        query = "SELECT * FROM  users WHERE id = %(user_id)s"

        results = connectToMySQL(cls.DB).query_db(query, {"user_id":user_id})

        return cls(results[0])


    
    # CREATE
    @classmethod
    def save(cls,data):
        query = """INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s)"""

        return connectToMySQL(cls.DB).query_db(query, data)
    
    # UPDATE
    @classmethod
    def update(cls,data):
        query = """UPDATE users 
                SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW()
                WHERE id = %(id)s"""
        return connectToMySQL(cls.DB).query_db(query,data)

    # DELETE
    @classmethod
    def delete(cls,user_id):
        query = """DELETE FROM users
                    WHERE id = %(user_id)s"""

        return connectToMySQL(cls.DB).query_db(query, {"user_id": user_id})