# test_atg_world.py

import requests
import unittest

class TestATGWorldWebsite(unittest.TestCase):

    def test_website_load(self):
        url = "https://atg.world"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()