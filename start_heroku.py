from flask import Flask
from ClassLawr_MongoDB import MongoDB
from ClassLawr_BotWebhook import BotWebhook

print('@@@@@@@@@@@@@@ ПРИВЕТ КОНСОЛЬ HEROKU @@@@@@@@@@@@@@')
app = Flask(__name__)
string = "mongodb+srv://Admin:HIUI#H*H89@pricecomparebot-mhmiv.mongodb.net/test?retryWrites=true&w=majority"
DB = MongoDB(connection_string=string, ssl=False)


@app.route('/')
def index():
    DB.add_line_to_end(dbs='Test', collection='Test', value={'Name': 'Test'})
    return '<h1>Hello Heroku!!@</h1>'
