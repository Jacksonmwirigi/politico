
from app.api.v2.models.base_model import BaseModel
from app.api.v2.db.db_config import* 
import jwt
from config import Config 
import datetime

class UserModel(BaseModel):
    def __init__(self,first_name="first_name", second_name="second_name",
     other_name="other_name", email="email", passportUrl="passport",
     phone_number="phone_number", isadmin="isadmin", iscandidate="iscandidate"):
        """creating user instance """
        self.first_name =first_name
        self.second_name =second_name
        self.other_name =other_name
        self.email =email
        self.phone_number =phone_number
        self.passportUrl=passportUrl
        self.isadmin =isadmin
        self.iscandidate =iscandidate

    def register_new(self,first_name, second_name, other_name, 
    email,passportUrl ,phone_number,isadmin, iscandidate):
        """This function registers a new user in the system."""
        # user = {
        #     "first_name": first_name,
        #     "second_name": second_name,
        #     "other_name": other_name,
        #     "email": email,
        #     "phone_number": phone_number,
        #     "passportUrl": passportUrl,
        #     "isAdmin": isAdmin,
        #     "isCandidate":isCandidate
        # }

        con = init_db()
        cur = con.cursor()

        if BaseModel().check_if_exists('users', 'passportUrl', passportUrl) ==True :
            """Checks for existing record of a user before registering a new account"""
            return "user is already registered"

        query = """ INSERT INTO users (first_name, second_name, 
        other_name, email,phone_number,passportUrl, isadmin,iscandidate) VALUES \
            ( '{}', '{}', '{}', '{}', '{}', '{}','{}','{}') RETURNING user_id """.format(first_name, second_name, 
        other_name, email,phone_number,passportUrl, isadmin,iscandidate)
        cur.execute(query)
        user_id = cur.fetchone()[0]
        con.commit()
        cur.close()
        return user_id

