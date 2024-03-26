from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Amber in 3308.'

# connection to database
@app.route('/db_test')
def testing():
	conn = psycopg2.connect("postgres://tin_db_user:tTiToULPV8Lk0GywTYolmJYineD40MUb@dpg-co0ekkol5elc738o47p0-a/tin_db")
	conn.close()
	return "Database Connection Successful"



