from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Flask, you better be worth it!'


if __name__ == '__main__':
	app.run()