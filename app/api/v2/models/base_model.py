from app.api.v2.db import db_config

class BaseMOdel:
    """THis is the base model class """
    def check_if_exists(self, table_name,field_name, value):
        """Checks for an existing record in the db"""

        con = init_db()
        cur = con.cursor()
        query = "SELECT * FROM {} WHERE {} ='{}';".format(table_name, field_name,value)
        cur.execute(query)
        response= cur.fetchall
        if response :
            return True 
        else :
            return False
         