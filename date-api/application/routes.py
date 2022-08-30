from application import app
from flask import Flask, request, Response
import random

@app.route('/get_date', methods=['GET'])
def date():
    date = random.choice(["2012-06-08", "2016-11-29", "2022-04-14"])
    return Response(date, mimetype='text/plain')