from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import views
from django.test import TestCase

class TestUrls(SimpleTestCase):
    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, views.loginPage)

    def test_create_account_url_resolves(self):
        url = reverse('create account')
        self.assertEqual(resolve(url).func, views.create_account)

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.index)

    def test_favorites_url_resolves(self):
        url = reverse('favorites')
        self.assertEqual(resolve(url).func, views.favorites)

    def test_restaurant_url_resolves(self):
        url = reverse('restaurant')
        self.assertEqual(resolve(url).func, views.restaurant)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, views.logoutUser)




