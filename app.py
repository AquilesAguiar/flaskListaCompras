from flask import Flask,render_template
import requests

app = Flask(__name__)

url = 'http://6b0b-35-185-107-52.ngrok.io/'

@app.route('/')
def index():
    req = requests.get(url)
    req = req.json()['products']
    return render_template('index.html',lista=req)


if __name__ == '__main__':
    app.run(debug=True)
