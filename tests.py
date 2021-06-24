import unittest
from main import app


# If you run the test a few times make sure to change the polynomial as it must be unique!
class TestPoly(unittest.TestCase):
    def test_upload_poly(self):
        client = app.test_client(self)
        response = client.post('/api/poly', data=dict(poly='x^2+y^3+x*y'))
        print(response.data)
        self.assertEqual(response.status_code, 200)


    def test_eval_poly(self):
        client = app.test_client(self)
        response = client.get('/api/poly/eval/?id=2&x=5&y=3')
        print(response.data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
