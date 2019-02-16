from app.db.new_db import Database
import psycopg2

class UserModeln():
    """creating a user object."""
    def __init__(self,first_name, second_name,other_name,passport_url, email_address ,phone_number, is_admin):
        """creating user class instance variables """
        self.first_name =first_name
        self.second_name =second_name
        self.other_name =other_name
        self.passport_url=passport_url
        self.email_address = email_address
        self.phone_number =phone_number
        self.is_admin =is_admin

    def register_user(self):
        """registers  a new user in the database -politicodb"""

        # reg_query = """INSERT INTO users (first_name, second_name,other_name, passport_url, email_address,phone_number, is_admin) VALUES(%(first_name)%,%(second_name)%,%(other_name)%, %(passport_url)% , %(email_address)%,%(phone_number)%,%(is_admin)%);"""

        query = """ INSERT INTO users (first_name, second_name,other_name, passport_url, email_address,phone_number, is_admin) VALUES \
                            ( %(first_name)s, %(second_name)s, %(other_name)s , %(passport_url)s , %(email_address)s, %(phone_number)s, %(is_admin)s) RETURNING user_id """
        con = Database().connection
        # cur = con.cursor()
        if con:
            cur =con.cursor()
            cur.execute(query)
            con.commit
            cur.close
        return  "new user created "   



        


