from app.api.v2.db.db_config import init_db
import psycopg2
from app.api.v2.models.base_model import BaseModel

con = init_db()
cur = con.cursor()

class Offices:
    """creating office object"""
    def __init__(self,office_name,office_type):
        """defining class instance variables."""
        self.office_name= office_name
        self.office_type =office_type

    def register_office(self):
        """Defining method for registering new party """
        regQry="INSERT INTO offices(office_name, office_type) VALUES (%s,%s)RETURNING *"   
        new_entry=(self.office_name,self.office_type) 
        cur.execute(regQry,new_entry)
        con.commit()
        new_office=cur.fetchall()
        return new_office

    @classmethod
    def get_all_offices(cls):
        """defines method for viewing all registered offices."""
        con = init_db()
        cur = con.cursor()
        get_query= """ SELECT * FROM offices""" 
        cur.execute(get_query)
        entries= cur.fetchall()
        return entries

    @classmethod
    def get_one_office(cls,office_id):
        """method for getting one specific government office by the office_id """
        cur.execute("""SELECT * FROM offices WHERE office_id='%s';"""%(office_id))  
        single_office =cur.fetchone()
        con.commit()
        return single_office
                      
