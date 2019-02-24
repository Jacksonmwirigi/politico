import unittest 
from app.api.v2.models.base_model import BaseModel
from app.api.v2.db.db_config import init_db

class TestUserModeln(unittest.TestCase):

    def test_decode_auth_token(self):
        new_user= UserModeln(
            first_name ="James",
            second_name = "NJuguna ",
            other_name = "test",
            passport_url  ="justicemuturi" ,
            email_address = "muturil@mail.com",
            phone_number = "6700" ,
            is_admin  = False
        )        
        # auth_token = new_user.encode_auth_token(new_user.user_id)
        # con = init_db()
        # cur = con.cursor()
        # cur.execute(auth_token)
        # con.commit()
        # cur.close()



        
      



    def test_decode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token) == 1)