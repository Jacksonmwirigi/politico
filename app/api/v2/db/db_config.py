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
	candidates = """ DROP TABLE IF EXISTS users CASCADE;  """

	queries = [users]

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
    IsAdmin Boolean varying(500) NOT NULL );"""

	candidates = """CREATE TABLE IF NOT EXISTS incidents (
    can_id serial PRIMARY KEY NOT NULL,
    candidate_name character varying(20) NOT NULL,
    office character varying(20) NOT NULL,
    party character varying(50)
    ); """

	queries = [candidates, users]
	return queries
