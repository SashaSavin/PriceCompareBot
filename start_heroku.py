from flask import Flask
from ClassLawr_MongoDB import MongoDB
from ClassLawr_BotWebhook import BotWebhook

print('@@@@@@@@@@@@@@ Hello Console PriceCompareBot @@@@@@@@@@@@@@')
app = Flask(__name__)
string = "mongodb+srv://Admin:HIUI#H*H89@pricecomparebot-mhmiv.mongodb.net/test?retryWrites=true&w=majority"
DB = MongoDB(connection_string=string, flag_ssl=False)


@app.route('/')
def index():
    document = {'Hello BD': 'PriceCompareBot'}
    DB.add_line_to_end(dbs='PriceCompareBot', collection='PriceCompareBot', value=document)
    return '@@@@@@@@@@@@@@ Hello Web PriceCompareBot @@@@@@@@@@@@@@'
