from flask import Flask
import pymongo
from ClassLawr_MongoDB import MongoDB
from ClassLawr_BotWebhook import BotWebhook

app = Flask(__name__)
string = "mongodb+srv://Admin:HIUI#H*H89@pricecomparebot-mhmiv.mongodb.net/test?retryWrites=true&w=majority"

DB = pymongo.MongoClient(string)
document = {'Hello BD': 'PriceCompareBot'}
coll = DB.CLIENT['PriceCompareBot']['PriceCompareBot']
coll.save(document)
print('@@@@@@@@@@@@@@ Hello Console PriceCompareBot @@@@@@@@@@@@@@')


@app.route('/')
def index():
    return '@@@@@@@@@@@@@@ Hello Web PriceCompareBot @@@@@@@@@@@@@@'
