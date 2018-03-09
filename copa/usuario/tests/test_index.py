from django.test import TestCase


# Create your tests here.
from copa.usuario.views import create_users, empty_form


class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'usuario/index.html')

    def test_has_method(self):
        self.assertTrue(create_users)

    def test_has_method_empty(self):
        self.assertTrue(empty_form)
