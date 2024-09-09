# items/tests.py

from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from .models import Item

User = get_user_model()

class ItemTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='root', password='Fisyb8o9h*2024')
	print(self.user)
        self.client.force_authenticate(user=self.user)  # Autenticación JWT
        self.item_data = {
            'reference': 'REF123',
            'name': 'Test Item',
            'description': 'Test Description',
            'price_without_tax': '100.00',
            'tax': '15.00'
        }

    def test_create_item(self):
        response = self.client.post('/api/items/', self.item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)

    def test_get_item(self):
        item = Item.objects.create(**self.item_data)
        response = self.client.get(f'/api/items/{item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Item')

