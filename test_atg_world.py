from selenium import webdriver
import unittest

class TestATGWorld(unittest.TestCase):
    def setUp(self):
        # Use webdriver.Chrome() without specifying executable_path
        self.driver = webdriver.Chrome()

    def test_website_loading(self):
        # Fix the indentation here
        driver = self.driver
        driver.get("https://atg.world")
        self.assertEqual(driver.title, "Across The Globe (ATG) - Professional and Personal Social Networking")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
