from application import app, db
from flask import Flask, request, render_template, url_for
from application.models import Books
import requests
from datetime import date


# home route
@app.route('/', methods = ['GET'])
def home():
    book_name = requests.get('http://book-api:5000/get_book_name')
    book_release_date = requests.get('http://date-api:5000/get_book_release_date')
    book_author = requests.post('http://author-api:5000/get_effect', json = {"Book": book_name.text, "Date": book_release_date.date})
    book = Books(book_name = event_name.text, book_release_date = book_release_date.date, book_author = author.text)
    db.session.add(book)
    db.session.commit()
    past5 = Books.query.order_by(Books.id.desc()).limit(5).all()
    return render_template('index.html', event = event, past5 = past5)