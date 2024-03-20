from selenium import webdriver
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.implicitly_wait(10)  # Set an implicit wait time for elements to load

    def tearDown(self):
        self.driver.quit()

    def test_example(self):
        self.driver.get("http://127.0.0.1:5000")  
        self.assertEqual(self.driver.title, "Example Domain")  # Replace with your expected title

if __name__ == '__main__':
    unittest.main()