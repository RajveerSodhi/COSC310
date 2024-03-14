import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from flask import Flask
app = Flask(__name__)

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()  # Initialize WebDriver

    def test_login_username_required(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000")  # Navigate to URL

        # Find the login button
        login_button = driver.find_element_by_id("submit")
        login_button.click()  # Click the login button

        # Find the error message or check the response for error indication
        error_message = driver.find_element_by_id("error_message")
        self.assertEqual(error_message.text, "Fill")

    def test_login_password_required(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000")  # Navigate to URL

        # Find the username field and enter a username
        username_field = driver.find_element_by_id("username")
        username_field.send_keys("testuser")

        # Find the login button
        login_button = driver.find_element_by_id("submit")
        login_button.click()  # Click the login button

        # Find the error message or check the response for error indication
        error_message = driver.find_element_by_id("error_message")
        self.assertEqual(error_message.text, "Password is required.")

    def tearDown(self):
        self.driver.quit()  # Clean up after the test

if __name__ == "_main_":
    unittest.main()