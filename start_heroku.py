from flask import Flask, request, jsonify
from ClassLawr_MongoDB import MongoDB
from ClassLawr_BotWebhook import BotWebhook

app = Flask(__name__)
string = "mongodb+srv://Admin:HIUI#H*H89@pricecomparebot-mhmiv.mongodb.net/test?retryWrites=true&w=majority"
DB = MongoDB(connection_string=string, flag_ssl=True)
token = "654597494:AAFvKQrYz8gw2cR5b5vVcMFzT7D8qI2j27Q"
url = "https://price-compare-bot.herokuapp.com/"
BOT = BotWebhook(token=token, web_address=url)
print('@@@@@@@@@@@@@@ Hello Console PriceCompareBot @@@@@@@@@@@@@@')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        document = {'Hello BD': 'PriceCompareBot'}
        DB.add_line_to_end(dbs='PriceCompareBot', collection='PriceCompareBot', value=document)
        return '@@@@@@@@@@@@@@ Hello Web PriceCompareBot @@@@@@@@@@@@@@'
    if request.method == 'POST':
        BOT.JSON = request.get_json()
        BOT.fast_send("@@@@@@@@@@@@@@ Hello Bot PriceCompareBot @@@@@@@@@@@@@@")
        return jsonify(BOT.JSON)
