import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()  # Initialize WebDriver

    def test_create_account_blank_email(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/signup")  # Navigate to Create Account URL

        # Find the create account button and click it without entering the email
        create_account_button = driver.find_element(By.ID, "create_account_button")
        create_account_button.click()  # Click the create account button

        # Check if the screen remains on the same page
        self.assertEqual(driver.current_url, "http://127.0.0.1:5000/signup", "Screen should remain on the same page")

    def test_create_account_blank_password(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/signup")  # Navigate to Create Account URL

        # Enter a username without entering the password
        username_field = driver.find_element(By.ID, "email")
        username_field.send_keys("testuser")

        # Find the create account button and click it without entering the password
        create_account_button = driver.find_element(By.ID, "create_account_button")
        create_account_button.click()  # Click the create account button

        # Check if the screen remains on the same page
        self.assertEqual(driver.current_url, "http://127.0.0.1:5000/signup", "Screen should remain on the same page")

    def test_create_account_blank_first_name(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/signup")  # Navigate to Create Account URL

        # Enter email and password but leave first name blank
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("test@example.com")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("password123")

        # Find the create account button and click it without entering the first name
        create_account_button = driver.find_element(By.ID, "create_account_button")
        create_account_button.click()  # Click the create account button

        # Check if the screen remains on the same page
        self.assertEqual(driver.current_url, "http://127.0.0.1:5000/signup", "Screen should remain on the same page")

    def test_create_account_blank_last_name(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/signup")  # Navigate to Create Account URL

        # Enter email, password, and first name but leave last name blank
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("test@example.com")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("password123")

        first_name_field = driver.find_element(By.ID, "firstName")
        first_name_field.send_keys("John")

        # Find the create account button and click it without entering the last name
        create_account_button = driver.find_element(By.ID, "create_account_button")
        create_account_button.click()  # Click the create account button

        # Check if the screen remains on the same page
        self.assertEqual(driver.current_url, "http://127.0.0.1:5000/signup", "Screen should remain on the same page")

    def tearDown(self):
        self.driver.quit()  # Clean up after the test

if __name__ == "__main__":
    unittest.main()

