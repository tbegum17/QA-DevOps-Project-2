from application import app
from flask import Flask, request, Response
import random

@app.route('/get_book_author', methods=['GET'])
def author():
    author = random.choice(["Taherah Mafi", "Ana Huang", "St Abby"])
    return Response(author, mimetype='text/plain')