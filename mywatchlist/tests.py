from django.test import TestCase

# Create your tests here.
class TestMyWatchlist(TestCase):
    def test_show_mywatchlist(self):
        response = self.client.get('/mywatchlist/')
        self.assertEqual(response.status_code, 200)

    def test_show_xml(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_show_json(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)

    def test_show_html(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)