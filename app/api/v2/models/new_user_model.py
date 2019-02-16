from app.api.v2.db.db_config import init_db
import psycopg2
from app.api.v2.models.base_model import BaseModel
# url = "postgresql://postgres:postgres@localhost/newpolitico"
# con = psycopg2.connect(url)
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
        con = init_db()
        cur = con.cursor()

 
        query = """ INSERT INTO users (first_name, second_name,other_name,passport_url,
        email_address,phone_number, is_admin) 
        VALUES(%s,%s, %s,%s , %s, %s, %s)"""

           

        new_entry = (self.first_name,self.second_name, self.other_name, 
        self.passport_url, self.email_address, self.phone_number, self.is_admin)
                       
        cur.execute(query, new_entry)
        con.commit()
        cur.close()
        return new_entry
    def get_all_users(self):
        con = init_db()
        cur = con.cursor()
        get_query= """ SELECT * FROM users ;""" 
        cur.execute(get_query)
        response= cur.fetchall
        return response

    