from flask import Flask
import requests
from datetime import datetime
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    url = "http://www.digikala.com"
    result = requests.get(url)
    return result.elapsed.total_seconds()
	#return 'Hello, World!'


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST' :
        url = request.form['url']
        user_count = request.form['user_count']
        result = requests.get('http://' + url)
        return result

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8009)