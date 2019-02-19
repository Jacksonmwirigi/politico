
import psycopg2
import os
# url for databse connection
url = "postgresql://postgres:postgres@localhost/newpolitico"
# return connection and creates tables
def init_db():
	con = psycopg2.connect(url)
	# con = connection(uri)
	cur = con.cursor()
	queries = tables()

	for query in queries:
		cur.execute(query)
	con.commit()
	return con


#test database connection
# def init_test_db(test_url):
   
# 	con = connection(test_uri)
# 	cur = con.cursor()
# 	queries = tables()

# 	for query in queries:
# 		cur.execute(query)
# 	con.commit()
# 	return con

# Deletes all tables after tests have been run
def destroydb():
	con = psycopg2.connect(url)
	cur = con.cursor()

	users = """ DROP TABLE IF EXISTS users CASCADE;  """
	candidates = """ DROP TABLE IF EXISTS candidates CASCADE;"""
	votes = """ DROP TABLE IF EXISTS votes CASCADE;  """
	parties = """ DROP TABLE IF EXISTS parties CASCADE;  """
	offices = """ DROP TABLE IF EXISTS offices CASCADE;  """

	queries = [candidates, users, votes, parties, offices]

	for query in queries:
		cur.execute(query)
	con.commit()

# contain all table creation queries
def tables():
	users = """ CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY NOT NULL,
    first_name  VARCHAR NOT NULL,
    second_name VARCHAR  NOT NULL,
    other_name VARCHAR NOT NULL,
    passport_url VARCHAR NOT NULL,
    email_address VARCHAR NOT NULL,
    phone_number Integer  NOT NULL,
    is_admin BOOLEAN  DEFAULT FALSE,
	password VARCHAR NOT NULL
	);"""
	

	# candidates = """CREATE TABLE IF NOT EXISTS candidates (
    # candidate_id serial PRIMARY KEY NOT NULL,
    # user_id integer REFERENCES users(user_id),
    # office_id integer REFERENCES office(office_id),
    # party_Id integer REFERENCES party(party_id),
	# date_created datestamp DEFAULT Now()
    # ); """

	parties = """ CREATE TABLE IF NOT EXISTS parties (
    party_id serial PRIMARY KEY NOT NULL,
    party_name character varying(50) NOT NULL,
    HQ_address character varying(50) NOT NULL,
    logo_Url character varying(50) NOT NULL,
    );"""
	

	# offices = """CREATE TABLE IF NOT EXISTS offices (
    # office_id serial PRIMARY KEY NOT NULL,
    # office_name character varying(20) NOT NULL,
    # office_type character varying(20) NOT NULL
    # ); """

	# votes = """CREATE TABLE IF NOT EXISTS votes (
    # vote_id serial PRIMARY KEY NOT NULL,
    # date_created timestamp varying(20) NOT NULL,
	# candidate_id integer REFERENCES candidate (candidate_id),
    # office_id integer REFERENCES office(office_id) 
    # ); """

	queries = [ users]
	return queries