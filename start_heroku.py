from flask import Flask
from ClassLawr_MongoDB import MongoDB
from ClassLawr_BotWebhook import BotWebhook

print('@@@@@@@@@@@@@@ Hello Console PriceCompareBot @@@@@@@@@@@@@@')
app = Flask(__name__)
string = "mongodb+srv://Admin:HIUI#H*H89@pricecomparebot-mhmiv.mongodb.net/test?retryWrites=true&w=majority"


@app.route('/')
def index():
    DB = MongoDB(connection_string=string, flag_ssl=False)
    document = {'Hello BD': 'PriceCompareBot'}
    coll = DB.CLIENT['PriceCompareBot']['PriceCompareBot']
    coll.save(document)
    return '@@@@@@@@@@@@@@ Hello Web PriceCompareBot @@@@@@@@@@@@@@'
