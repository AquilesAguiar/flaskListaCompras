from flask import Flask,render_template
import requests

app = Flask(__name__)


# listaCompras = {
#     0:['Abobora','43,43','https://st.depositphotos.com/1011268/1307/i/600/depositphotos_13077441-stock-photo-pumpkin.jpg'],
#     1:[],
#     2:[],
#     3:[],
#     4:[],
#     5:[],
#     6:[],
#     7:[],
#     8:[],
#     9:[],

# }

url = 'http://6b0b-35-185-107-52.ngrok.io/'

@app.route('/')
def index():
    req = requests.get(url)
    req = req.json()['products']
    return render_template('index.html',lista=req)


if __name__ == '__main__':
    app.run(debug=True)
