from django.test import TestCase
from django.urls import resolve
from CV.views import cv_page

class CVPageTest(TestCase):
	def test_cv_url_found(self):
		found = resolve('/cv/')
		self.assertEqual(found.func, cv_page)

	def test_cv_uses_template(self):
		response = self.client.get('/cv/')
		self.assertTemplateUsed(response, 'cv.html')
