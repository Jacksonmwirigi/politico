import psycopg2
import os
DB_NAME="politicodb"
DB_PASSWORD="postgres"
DB_HOST= "localhost"
DB_USER="postgres"
url= "postgresql://postgres:postgres@localhost/politicodb"

#conn = psycopg2.connect(host="localhost", port=5432, database="politicodb", user="postgres", password="postgres")
class Database():
    def __init__(self):
        self.connection=psycopg2.connect(url)
        
    def create_tables(self):
        commands = (

        """
        CREATE TABLE users (
                user_id INTEGER PRIMARY KEY,
                first_name VARCHAR NOT NULL,
                second_name VARCHAR NOT NULL,
                other_name VARCHAR NOT NULL,
                passport_url VARCHAR NOT NULL,
                email_address VARCHAR NOT NULL,
                phone_number VARCHAR NOT NULL,
                is_admin BOOLVARCHAR  NOT NULL

                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
            """
        CREATE TABLE parties (
                party_id INTEGER PRIMARY KEY,
                hq_address VARCHAR(5) NOT NULL,
                logo_url VARCHAR NOT NULL

                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
        )
        try:
            conn=self.connection 
            cur = conn.cursor()
            # create table one by one
            for command in commands:
                cur.execute(command)
                print ("tables created successfully")
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
       