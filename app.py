import psycopg2
from flask import Flask
from flask import Flask, render_template


app = Flask(__name__)


# URLs for website pages, listed in index page
pages = [
    {"name": "Index", "url": "/"},
    {"name": "Database Test", "url": "/db_test"},
    {"name": "Create Table", "url": "/db_create"},
	{"name": "Insert Table Values", "url": "/db_insert"},
	{"name": "Select Table Values", "url": "/db_select"},
	{"name": "Drop Table", "url": "/db_drop"}
]

# hello world index page
@app.route('/')
def hello_world():
    return 'Hello World from Amber in 3308.' + render_template('index.html', pages=pages)

# connection to database
@app.route('/db_test')
def testing():
	conn = psycopg2.connect("postgres://tin_db_user:tTiToULPV8Lk0GywTYolmJYineD40MUb@dpg-co0ekkol5elc738o47p0-a/tin_db")
	conn.close()
	return "Database Connection Successful"

# create basketball table
@app.route('/db_create')
def creating():
	conn = psycopg2.connect("postgres://tin_db_user:tTiToULPV8Lk0GywTYolmJYineD40MUb@dpg-co0ekkol5elc738o47p0-a/tin_db")
	cur = conn.cursor()
	cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
	''')
	conn.commit()
	conn.close()
	return "Basketball Table Successfully Created"

# insert values into basketball table
@app.route('/db_insert')
def inserting():
	conn = psycopg2.connect("postgres://tin_db_user:tTiToULPV8Lk0GywTYolmJYineD40MUb@dpg-co0ekkol5elc738o47p0-a/tin_db")
	cur = conn.cursor()
	cur.execute('''
	INSERT INTO Basketball (First, Last, City, Name, Number)
	Values
	('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
	('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
	('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
	('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
	''')
	conn.commit()
	conn.close()
	return "Basketball Table Populated"

# query all the data from the table
@app.route('/db_select')
def selecting():
	conn = psycopg2.connect("postgres://tin_db_user:tTiToULPV8Lk0GywTYolmJYineD40MUb@dpg-co0ekkol5elc738o47p0-a/tin_db")
	cur = conn.cursor()
	cur.execute('''
	SELECT * FROM Basketball;
	''')
	# capture results of query
	records = cur.fetchall()
	conn.close()
	response_string="" 
	# format records as a table
	response_string+="<table>"
	for player in records:
		response_string+="<tr>"
		for info in player:
			response_string+="<td>{}</td>".format(info)
		response_string+="<tr>"
	response_string+="<table>"
	return response_string

# drop basketball table from the database
@app.route('/db_drop')
def dropping():
	conn = psycopg2.connect("postgres://tin_db_user:tTiToULPV8Lk0GywTYolmJYineD40MUb@dpg-co0ekkol5elc738o47p0-a/tin_db")
	cur = conn.cursor()
	cur.execute('''
		DROP TABLE Basketball;
	''')
	conn.commit()
	conn.close()
	return "Basketball Table Successfully Dropped"
