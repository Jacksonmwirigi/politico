from app.api.v2.db.db_config import init_db
import psycopg2
from app.api.v2.models.base_model import BaseModel

con = init_db()
cur = con.cursor()
class UserModel():
    """creating a user object."""
    def __init__(self,first_name, second_name,other_name,passport_url, 
    email_address ,phone_number, is_admin,password):
        """creating user class instance variables """
        self.first_name =first_name
        self.second_name =second_name
        self.other_name =other_name
        self.passport_url=passport_url
        self.email_address = email_address
        self.phone_number =phone_number
        self.is_admin =is_admin
        self.password=password     

    def register_user(self):
        """registers  a new user in the database -politicodb"""
        con = init_db()
        cur = con.cursor()
 
        query = """ INSERT INTO users (first_name, second_name,other_name,passport_url,
        email_address,phone_number, is_admin,password) 
        VALUES(%s,%s, %s,%s , %s, %s, %s,%s)"""  
                 
        new_entry = (self.first_name,self.second_name, self.other_name, 
        self.passport_url, self.email_address, self.phone_number, self.is_admin, self.password)
        
        cur.execute(query, new_entry)
        con.commit()
        cur.close()
        return new_entry
            
    @classmethod  
    def get_all_users(cls):
        """defines method for viewing all registered users."""
        con = init_db()
        cur = con.cursor()
        get_query= """ SELECT * FROM users""" 
        cur.execute(get_query)
        users= cur.fetchall()
        return users

    @classmethod
    def user_login(cls, phone_number):
        """Defines user login method"""
        login_query=""" SELECT phone_number FROM users WHERE phone_number=%s"""
        cur.execute(login_query) 
        loged_user= cur.fetchone(phone_number)
        return loged_user

    @classmethod
    def get_email_address(cls, email_address):
        """Gets specific user's email address to allow login"""
        cur.execute("""SELECT * FROM users WHERE email_address='%s'"""%(email_address))  
        user =cur.fetchone()
        con.commit()
        return user
    @classmethod    
    def delete_user(cls,email):
        delete_query= "DELETE FROM users WHERE email_address =%s RETURNING *;"
        cur.execute(delete_query,(email,))
        new=cur.fetchall()
        con.commit()
        return new
    @classmethod    
    def update_user_data(cls, fname,sname,phone,email,):
        if BaseModel().check_if_exists('users','email_address',email):
            update_query= "UPDATE users set first_name =%s,second_name=%s,phone_number\
                 =%s WHERE email_address=%s RETURNING *;"
            cur.execute(update_query,(fname,sname,phone, email))
            con.commit()
            newname=cur.fetchall()
            return newname
        else:
            return None

        


       