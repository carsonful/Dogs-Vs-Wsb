from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import sleep
from time import time
from random import random
from flask import Flask, render_template, make_response
from extensions import portfolios


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('https://dogs-vs-wsb.herokuapp.com/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity]

    sleep(150)

    Temperature = portfolios.myround(portfolios.dogequity())
    Humidity = portfolios.myround(portfolios.wsbequity())

    data = [time() * 1000, Temperature, Humidity]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", prot=5000, debug=True)
