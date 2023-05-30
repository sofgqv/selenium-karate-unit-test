import unittest
from app import app
import json

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.app = app #de server
        self.client = self.app.test_client

        self.fizz = "3"
        self.buzz = "5"
        self.fizzbuzz = "15"
        self.none = "7"
        self.zero = "0"
        self.error = "hola"

    def test_notfound(self):
        response = self.client().get('/fzzbzz')
        self.assertEqual(response.status_code, 404)

    def test_empty(self):
        response = self.client().get('/fizzbuzz')
        data = json.loads(response.data)
        self.assertEqual(data['statusCode'], 500)

    def test_fizz(self):
        response = self.client().get('/fizzbuzz?input=' + self.fizz)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 'Fizz')
    
    def test_buzz(self):
        response = self.client().get('/fizzbuzz?input=' + self.buzz)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 'Buzz')

    def test_fizzbuzz(self):
        response = self.client().get('/fizzbuzz?input=' + self.fizzbuzz)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 'FizzBuzz')
    
    def test_zero(self):
        response = self.client().get('/fizzbuzz?input=' + self.zero)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 'FizzBuzz')

    def test_none(self):
        response = self.client().get('/fizzbuzz?input=' + self.none)
        data = json.loads(response.data)
        self.assertEqual(data['result'], int(self.none))
    
    def test_error(self):
        response = self.client().get('/fizzbuzz?input=' + self.error)
        data = json.loads(response.data)
        self.assertEqual(data['statusCode'], 500)