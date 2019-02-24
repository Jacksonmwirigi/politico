from app.api.v2.db.db_config import init_db

con = init_db()
cur = con.cursor()

class Candidates():
    def __init__(self,user_id,office_id,party_id,date_created):
        self.user_id=user_id
        self.office_id=office_id
        self.party_id=party_id
        self.date_created=date_created

    def register_candidate(self):
        regQry="INSERT INTO candidates(user_id,office_id,party_id,date_created)\
            VALUES(%s,%s,%s,%s)RETURNING *;"  
        entry=(self.user_id,self.office_id,self.party_id,self.date_created)    
        cur.execute(regQry,entry)
        con.commit()
        cand_new=cur.fetchall()
        return cand_new      
            