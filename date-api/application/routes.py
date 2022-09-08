from application import app
from flask import Flask, request, Response
import random


@app.route('/get_book_date', methods=['POST'])
def date():
    return Response(random.choice(["2012-06-08", "2016-11-29", "2022-04-14"]), mimetype='text/plain')