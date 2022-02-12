from urllib import request
from django.test import TestCase
from django.http import HttpRequest
from snippets.views import top

class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        # HttpRequestのオブジェクト作成
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, b"Hello World")
