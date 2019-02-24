from app.api.v2.db.db_config import init_db
import psycopg2
from app.api.v2.models.base_model import BaseModel

con = init_db()
cur = con.cursor()

class Parties():
    """creating a party object"""
    def __init__(self, party_name, hq_address, logo_url):
        """Defining class instance variables"""
        self.party_name= party_name
        self.hq_address=hq_address
        self.logo_url= logo_url

    def register_party(self):
        """adding new party record into db"""
        reg_qry= "INSERT INTO parties (party_name, hq_address, logo_url )\
             VALUES(%s,%s,%s) RETURNING *;"    

        new_entry=(self.party_name,self.hq_address,self.logo_url)     
        cur.execute(reg_qry,new_entry)
        con.commit()
        new_party=cur.fetchall()
        return new_party

    @classmethod
    def view_all_parties(cls):
        """DEfines method to diplay all regitered parties"""
        vw_qry= "select * from parties;"
        cur.execute(vw_qry)
        con.commit()
        entries=cur.fetchall()
        return entries

    @classmethod
    def get_one_party(cls,party_id):
        """method for getting one specific party by the party_id  """
        cur.execute("""SELECT * FROM parties WHERE party_id='%s';"""%(party_id))  
        single_party =cur.fetchone()
        con.commit()
        return single_party
                  