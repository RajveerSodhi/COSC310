# selenium_utils.py
from selenium import webdriver

def perform_selenium_actions():
    # Initialize WebDriver
    driver = webdriver.Chrome('/path/to/chromedriver')

    # Example Selenium actions
    driver.get('https://example.com')
    title = driver.title

    # Close the WebDriver
    driver.quit()

    return title
