from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

"""
@app.route('/check/<url>')
def check(url):
    return render_template('hello.html', name=name)
"""

