import psycopg2
import os

# url for databse connection
uri = os.getenv(['DATABASE_URL'])

# url for test databse connection
test_uri = os.getenv(['DATABASE_TEST_URL'])


# return connection
def connection(url):
	con = psycopg2.connect(url)
	return con


# return connection and creates tables
def init_db():
	con = connection(uri)
	cur = con.cursor()
	queries = tables()

	for query in queries:
		cur.execute(query)
	con.commit()
	return con


# return connection and creates tables (TDD)
def init_test_db(test_url):
	con = connection(test_uri)
	cur = con.cursor()
	queries = tables()

	for query in queries:
		cur.execute(query)
	con.commit()
	return con

# Deletes all tables after tests have been run
def destroydb():
	con = connection(test_uri)
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
    first_name character varying(50) NOT NULL,
    second_name character varying(50) NOT NULL,
    other_name character varying(50) NOT NULL,
    email character varying(50),
    phone_number Integer varying(50) NOT NULL,
    passportUrl character varying(50) NOT NULL,
    isAdmin BOOLEAN varying(500) DEFAULT FALSE, 
	isCandidate BOOLEAN DEFAULT FALSE);"""
	

	candidates = """CREATE TABLE IF NOT EXISTS incidents (
    candidate_id serial PRIMARY KEY NOT NULL,
    user_id integer REFERENCES users(user_id),
    office_id integer REFERENCES office(office_id),
    party_Id integer REFERENCES party(party_id),
	date_created datestamp DEFAULT Now()
    ); """

	parties = """ CREATE TABLE IF NOT EXISTS party (
    party_id serial PRIMARY KEY NOT NULL,
    party_name character varying(50) NOT NULL,
    HQ_address character varying(50) NOT NULL,
    logo_Url character varying(50) NOT NULL,
    );"""
	

	offices = """CREATE TABLE IF NOT EXISTS office (
    office_id serial PRIMARY KEY NOT NULL,
    office_name character varying(20) NOT NULL,
    office_type character varying(20) NOT NULL
    ); """

	votes = """CREATE TABLE IF NOT EXISTS vote (
    vote_id serial PRIMARY KEY NOT NULL,
    date_created timestamp varying(20) NOT NULL,
	candidate_id integer REFERENCES candidate (candidate_id),
    office_id integer REFERENCES office(office_id) 
    ); """

	queries = [candidates, users, votes, parties, offices]
	return queries

