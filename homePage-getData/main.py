from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    url = "http://digikala.com"
    result = requests.get(url).content
    return result
	#return 'Hello, World!'

@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST' :
        url = request.form['url']
        url = "digikala.com"
        user_count = request.form['user_count']
        result = request.get(url)
        return result

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8009)