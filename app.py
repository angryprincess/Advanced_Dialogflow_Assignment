from flask import Flask, request
from datetime import datetime
import json
import requests
app = Flask(__name__)
app.debug = True


#@app.route('/webhook', methods=['POST'])
@app.route('/')
def index():
    body = request.json
    
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q=Toronto&units=metric&appid=19bc09406ba467d4ea980ffe2deca519'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_url, headers=headers)
    r=response.json()

    city = body['queryResult']['parameters']['geo-city']
    temp = str(int(r['main']['temp']))
    sunrise = str(r["sys"]["sunrise"])
    ts = int(sunrise)
    utchour = int(datetime.utcfromtimestamp(ts).strftime('%H'))
    duskhour = utchour-4
    strduskhour = str(duskhour)
    reply = '{"fulfillmentMessages": [ {"text": {"text": ["The temperature in ' + city +',  is  '+ temp + ' and the sunrise time is ' + strduskhour + ' AM."] } } ] }'
    return reply

if __name__ == '__main__':
    app.run()
