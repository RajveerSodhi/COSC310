#from selenium.webdriver import Firefox, FirefoxOptions
#from selenium.webdriver.firefox.service import Service as FirefoxService
#from webdriver_manager.firefox import GeckoDriverManager

#options = FirefoxOptions()
#options.binary ='C:/Program Files/Mozilla Firefox/firefox.exe' # on Windows

#driver = Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
#driver.get('https://www.google.com')


import unittest
from flask import Flask, url_for
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
        self.driver = webdriver.Firefox()  # Initialize WebDriver

    def test_login_username_required(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000")  # Navigate to URL

        # Find the login button and click it without entering username/password
        login_button = driver.find_element(By.ID, "submit")
        login_button.click()  # Click the login button

        # Check if the login form is still visible
        login_form = driver.find_element(By.TAG_NAME, "form")
        self.assertTrue(login_form.is_displayed(), "Login form should still be visible")

    def test_login_password_required(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000")  # Navigate to URL

        # Find the username field and enter a username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("testuser")

        # Find the login button and click it without entering the password
        login_button = driver.find_element(By.ID, "submit")
        login_button.click()  # Click the login button

        # Check if the login form is still visible
        login_form = driver.find_element(By.TAG_NAME, "form")
        self.assertTrue(login_form.is_displayed(), "Login form should still be visible")

    def tearDown(self):
        db.session.remove()  # Remove the session
        db.drop_all()  # Drop all tables

    def test_login_submission(self):
        # Simulate a user submitting login information
        with self.client:
            response = self.client.post('/login', data={'username': 'stu@gmail.com', 'password': '1'})

            # Check if the response is a redirect (assuming successfully
            expected_url = url_for('views.home', _external=True)  
            self.assertRedirects(response, expected_url)



            # Check if the user's info is saved in the database
            user = User.query.filter_by(username='stu@gmail.com').first()
            self.assertIsNotNone(user)  # Check if user exists
            self.assertEqual(user.password, '1')  # Check if password is correct

if __name__ == '__main__':
    unittest.main()
