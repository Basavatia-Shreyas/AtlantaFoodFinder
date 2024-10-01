from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import views
from django.test import TestCase
from .templates.forms import CreateUserForm
from django.contrib.auth.models import User

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

class TestUrls2(TestCase):
    def test_non_existent_url(self):
        response = self.client.get('/non-existent-url/')
        self.assertEqual(response.status_code, 404)

    def setUp(self):
        self.url = reverse('create account')

    def test_weak_password_length(self):
        data = {
            'username': 'user',
            'password1': 'django',
            'password2': 'django',
            'cuisine': 'Italian'
        }
        response = self.client.post(self.url, data)

        form = CreateUserForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('password must contain at least 8 characters.', form.errors['password1'])

        self.assertFalse(User.objects.filter(username='user').exists())

    def test_weak_password_numerical(self):
        data = {
            'username': 'user2',
            'password1': '12345678',
            'password2': '12345678',
            'cuisine': 'Mexican'
        }
        response = self.client.post(self.url, data)

        form = CreateUserForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('[password is all numerical].', form.errors['password1'])

        self.assertFalse(User.objects.filter(username='user2').exists())
