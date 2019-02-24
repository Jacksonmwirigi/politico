from app.api.v2.db.db_config import init_db
import psycopg2
from app.api.v2.models.base_model import BaseModel

con = init_db()
cur = con.cursor()

class Offices:
    def __init__(self,office_name,office_type):
        self.office_name= office_name
        self.office_type =office_type

    def register_office(self):
        regQry="INSERT INTO offices(office_name, office_type) VALUES (%s,%s)RETURNING *"   
        new_entry=(self.office_name,self.office_type) 
        cur.execute(regQry,new_entry)
        con.commit()
        new_office=cur.fetchall()
        return new_office
