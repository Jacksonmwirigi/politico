# import psycopg2
# import os
# DB_NAME="politicodb"
# DB_PASSWORD="postgres"
# DB_HOST= "localhost"
# DB_USER="postgres"
# url= "postgresql://postgres:postgres@localhost/newpolitico"

# #conn = psycopg2.connect(host="localhost", port=5432, database="politicodb", user="postgres", password="postgres")
# class Database():
#     def __init__(self):
#         self.connection=psycopg2.connect(url)

        
#     def create_tables(self):
       
#         new_table = """CREATE TABLE users (
#             user_id INTEGER PRIMARY KEY,
#             first_name VARCHAR NOT NULL,
#             second_name VARCHAR NOT NULL,
#             other_name VARCHAR NOT NULL,
#             passport_url VARCHAR NOT NULL,
#             email_address VARCHAR NOT NULL,
#             phone_number VARCHAR NOT NULL,
#             is_admin VARCHAR  NOT NULL

#             ON UPDATE CASCADE ON DELETE CASCADE
#         )
#         """

#         conn=self.connection 
#         if conn:
#             print ("am connected already")
#             cur = conn.cursor()
#             cur.execute(new_table)
#             cur.close()
#         else :
#             print ("am not connected")    

#             # commit the 
#         # try:
#         #     conn=self.connection 
#         #     cur = conn.cursor()
#         #     # create table one by one
#         #     # for command in commands:
#         #     cur.execute(new_table)
#         #     print ("tables created successfully")
#         #     # close communication with the PostgreSQL database server
#         #     cur.close()
#         #     # commit the changes
#         #     conn.commit()
#         # except:
#         #     print("error occures")
#         # finally:
#         #     if conn is not None:
#         #         conn.close()
# db=Database()
# db.create_tables       