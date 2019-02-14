from app.api.v2.db.db_config import *
import jwt
import datetime

class BaseModel:
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

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                os.getenv('SECRET'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """Validates the auth token :param auth_token::return: integer|string"""
        try:
            payload = jwt.decode(auth_token, os.getenv('SECRET'))
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
           return 'Invalid token. Please log in again.'    

