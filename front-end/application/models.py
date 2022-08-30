from application import db 

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(50))
    book_release_date = db.Column(db.DateTime)
    book_author = db.Column(db.String(50))
    def __str__(self):
        return f"{self.book_name}: {self.book_release_date} {self.book_author}"