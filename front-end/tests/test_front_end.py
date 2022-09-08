from flask import url_for
from flask_testing import TestCase
from datetime import date
import requests_mock
import pytest
# import the app's classes and objects
from application import app, db
from application.models import Books

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                DEBUG=True,
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test book
        sample1 = Books(book_name="Shatter Me", book_author="Taherah Mafi", book_release_date="2012-06-08")

        # save book to database
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()