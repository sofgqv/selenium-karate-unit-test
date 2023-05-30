import unittest
from python.api import app
import json

class TestPeliculasApi(unittest.TestCase):
    def setUp(self):
        self.app = app() #de server
        self.client = self.app.test_client

        self.fizz = {
            "input" : 3
        }

        self.buzz=  {
            "input" : 5
        }

        self.fizzbuzz =  {
            "input" : 15
        }

        self.none =  {
            "input" : 7
        }

    def test_fizz(self):
        response = self.client().post('/fizzbuzz', json=self.fizz)
        data = json.loads(response.data)
        print('data: ', data)

        self.assertEqual(data['result'], 'Fizz')
