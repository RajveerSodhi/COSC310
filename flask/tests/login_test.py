import unittest
from flask import Flask
from flask_testing import TestCase
from website.models import db, User  # Import the database and the User model

# sys.path.append('flask\main.py')  # Replace '/path/to/myapp' with the actual path to the 'myapp' package or module

# Still under Construction
from main import create_app
from flask import app


  # Import your Flask app and database setup

class TestLoginPage(TestCase):
    def create_app(self):
        app = create_app()  # Assume you have different configurations, including a 'testing' config
        return app

    def setUp(self):
        db.create_all()  # Create database tables

    def tearDown(self):
        db.session.remove()  # Remove the session
        db.drop_all()  # Drop all tables

    def test_login_submission(self):
        # Simulate a user submitting login information
        with self.client:
            response = self.client.post('/login', data={'username': 'testuser', 'password': 'testpassword'})

            # Check if the response is a redirect (assuming successful login redirects somewhere)
            self.assert_redirects(response, '/')

            # Check if the user's info is saved in the database
            user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(user)  # Check if user exists
            self.assertEqual(user.password, 'testpassword')  # Check if password is correct

if __name__ == '__main__':
    unittest.main()
