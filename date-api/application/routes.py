from application import app
from flask import Flask, request, Response

@app.route('/get_date', methods=['POST'])
def date():
    book_data = request.get_json()
    book_name = book_data["Book Name"]
    book_author = book_data["Book Author"]
    date = {"2012-06-08", "2016-11-29", "2022-04-14"}
    return Response(date, mimetype='text/plain')