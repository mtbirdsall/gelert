from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/gelert'

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(80), unique = True)

	def __init__(self, username, emial):
		self.username = username
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.username



@app.route('/')
def index():
	return 'Flask, you better be worth it!'


if __name__ == '__main__':
	app.run()