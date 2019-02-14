from app.api.v2.db import db_config
from app.api.v2.models.base_model import BaseMOdel

class UserModel(BaseMOdel):
    def __init__(self, first_name, second_name, other_name, email, passportUrl ,phone_number,isAdmin, isCandidate):
        """creating user instance """
        self.first_name =first_name
        self.second_name =second_name
        self.other_name =other_name
        self.email =email
        self.phone_number =phone_number
        self.passportUrl=passportUrl
        self.isAdmin =isAdmin
        self.isCandidate =isCandidate

    def save(self):
        """This function registers a new user in the system."""
        user = {
            "first_name": self.first_name,
            "second_name": self.second_name,
            "other_name": self.other_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "passportUrl": self.passportUrl,
            "isAdmin": self.isAdmin,
            "isCandidate": self.isCandidate
    
        }

        con = init_db()
        cur = con.cursor()

        if BaseMOdel().check_if_exists('users', 'passportUrl', self.passportUrl) ==True :
            """Checks for existing record of a user before registering a new account"""
            return "user is already registered"

        query = """ INSERT INTO users (first_name, second_name, other_name, email,phone_number,passportUrl, isAdmin,isCandidate) VALUES \
                "other_name": self.other_name,
                    ( %(first_name)s, %(second_name)s, %(other_name)s,%(email)s, %(phone_number)s, %(passportUrl)s,%(isAdmin)s, %(isCandidate)s) RETURNING user_id """
        cur.execute(query, user)
        user_id = cur.fetchone()[0]
        con.commit()
        cur.close()
        return user_id
