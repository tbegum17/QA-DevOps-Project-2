from application import app
from flask import Flask, request, Response
import random

@app.route('/get_book', methods = ['GET'])
def book():
    book_name = random.choice(["Shatter Me", "Twisted Love", "The Risk"]) 
    return Response(book_name, mimetype='text/plain')