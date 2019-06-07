from flask import Flask
from ClassLawr_MongoDB import MongoDB
import os

print('@@@@@@@@@@@@@@ ПРИВЕТ КОНСОЛЬ HEROKU @@@@@@@@@@@@@@')
app = Flask(__name__)
string = "mongodb+srv://Admin:P13hesheshes@botonlnr-h6f2t.mongodb.net/test?retryWrites=true&w=majority"
DB = MongoDB(connection_string=string, ssl=False)


@app.route('/')
def index():
    DB.add_line_to_end(dbs='glacial-escarpment-41321', collection='Test', value={'Name': 'Pet'})
    return '<h1>Hello Heroku!!@</h1>'
