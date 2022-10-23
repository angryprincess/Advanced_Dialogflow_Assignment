from flask import Flask, request
from datetime import datetime
import json
import requests
app = Flask(__name__)
app.debug = True


@app.route('/webhook', methods=['POST'])
def index():
    body = request.json
    
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q=Toronto&units=metric&appid=19bc09406ba467d4ea980ffe2deca519'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_url, headers=headers)
    r=response.json()

    city = body['queryResult']['parameters']['geo-city']
    temp = str(int(r['main']['temp']))
    sunsrise = str(r["sys"]["sunrise"])
    ts = int(sunsrise)
    utchour=int(datetime.utcfromtimestamp(ts).strftime('%H'))
    duskhour = utchour-4
    reply = '{"fulfillmentMessages": [ {"text": {"text": ["The temperature in ' + city +',  is  '+ temp + ' and the sunrise time is ' + duskhour + ' AM."] } } ] }'
    return reply

if __name__ == '__main__':
    app.run()