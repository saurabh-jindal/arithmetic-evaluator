from django.test import TestCase, Client

class APITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_evaluate_expression_valid(self):
        response = self.client.post('/evaluate/', {'expression': '5+3-2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 6)

    def test_evaluate_expression_invalid_format(self):
        response = self.client.post('/evaluate/', {'expression': '5+3*2'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid expression format.', response.json().get('error'))

    def test_evaluate_expression_missing(self):
        response = self.client.post('/evaluate/')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Expression is missing.', response.json().get('error'))

    def test_evaluate_expression_method_not_allowed(self):
        response = self.client.get('/evaluate/')
        self.assertEqual(response.status_code, 405)
